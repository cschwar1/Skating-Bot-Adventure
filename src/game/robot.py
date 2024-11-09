from utils.constants import WIDTH, HEIGHT, BLUE
from utils.assets import draw_robot
from utils.audio import audio_manager

class Robot:
    """
    Represents the player-controlled robot in the Skating Bot Adventure game.

    This class manages the robot's position, movement, jumping, acrobatics,
    and interaction with obstacles.

    Attributes:
        x (float): The x-coordinate of the robot's position.
        y (float): The y-coordinate of the robot's position.
        width (int): The width of the robot's hitbox.
        height (int): The height of the robot's hitbox.
        speed (float): The horizontal movement speed of the robot.
        jump_power (float): The initial vertical velocity when jumping.
        velocity_y (float): The current vertical velocity of the robot.
        is_jumping (bool): Whether the robot is currently in a jump.
        acrobatic_state (int): The current acrobatic state (0-2).
        acrobatic_cooldown (int): Cooldown timer for performing acrobatics.
        score (int): The player's current score.
        lives (int): The number of lives remaining.
        invincibility_timer (int): Timer for invincibility after taking damage.
    """

    def __init__(self, x, y):
        """
        Initialize a new Robot instance.

        Args:
            x (float): The initial x-coordinate of the robot.
            y (float): The initial y-coordinate of the robot.
        """
        self.x = x
        self.y = y
        self.width = 50
        self.height = 50
        self.speed = 5
        self.jump_power = 15
        self.velocity_y = 0
        self.is_jumping = False
        self.acrobatic_state = 0
        self.acrobatic_cooldown = 0
        self.score = 0
        self.lives = 3
        self.invincibility_timer = 0

    def draw(self, canvas):
        """
        Draw the robot on the given canvas.

        If the robot is invincible, it will blink (alternate visibility).

        Args:
            canvas: The Kivy canvas to draw on.
        """
        if self.invincibility_timer > 0 and self.invincibility_timer % 10 < 5:
            return  # Create a blinking effect when invincible
        draw_robot(canvas, self.x, self.y, self.width, self.height)

    def move(self, dx):
        """
        Move the robot horizontally.

        Args:
            dx (int): The direction of movement (-1 for left, 1 for right).
        """
        self.x += dx * self.speed
        self.x = max(0, min(self.x, WIDTH - self.width))

    def jump(self):
        """
        Make the robot jump if it's not already jumping.
        """
        if not self.is_jumping:
            self.velocity_y = -self.jump_power
            self.is_jumping = True
            audio_manager.play_jump_sound()

    def perform_acrobatics(self):
        """
        Perform an acrobatic move if conditions are met.

        Acrobatics can only be performed while jumping and when the cooldown is zero.
        """
        if self.is_jumping and self.acrobatic_cooldown == 0:
            self.acrobatic_state = (self.acrobatic_state + 1) % 3
            self.acrobatic_cooldown = 30
            self.score += 10 * (self.acrobatic_state + 1)  # More points for complex acrobatics
            audio_manager.play_acrobatic_sound()

    def update(self, obstacles):
        """
        Update the robot's state, including position, collisions, and timers.

        Args:
            obstacles (list): A list of Obstacle objects to check for collisions.
        """
        self.y += self.velocity_y
        if self.is_jumping:
            self.velocity_y += 1  # Gravity
        
        # Check for collision with obstacles
        for obstacle in obstacles:
            if obstacle.collide(self):
                if self.velocity_y > 0:
                    self.y = obstacle.y - self.height
                    self.is_jumping = False
                    self.velocity_y = 0
                    if isinstance(obstacle, Slope):
                        self.perform_acrobatics()  # Automatically perform acrobatics on slopes
                elif self.invincibility_timer == 0:
                    self.lives -= 1
                    self.invincibility_timer = 60  # 1 second of invincibility
                    audio_manager.play_collision_sound()
                break
        else:
            if self.y >= HEIGHT - self.height:
                self.y = HEIGHT - self.height
                self.is_jumping = False
                self.velocity_y = 0

        if self.acrobatic_cooldown > 0:
            self.acrobatic_cooldown -= 1

        if self.invincibility_timer > 0:
            self.invincibility_timer -= 1

        # Increase score over time
        self.score += 1