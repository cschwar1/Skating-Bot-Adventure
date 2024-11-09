import random
from utils.constants import WIDTH, HEIGHT, RED, GREEN, BROWN
from utils.assets import draw_snowball, draw_ice_block, draw_slope

class Obstacle:
    def __init__(self, x, y, width, height, color, obstacle_type="normal"):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.type = obstacle_type
        self.melting = False
        self.melt_speed = 0.5
        self.move_direction = random.choice([-1, 1])
        self.move_speed = random.uniform(0.5, 2)
        self.separation_cooldown = 0

    def draw(self, canvas):
        if self.type == "snowball":
            draw_snowball(canvas, self.x, self.y, self.width, self.height)
        elif self.type == "ice_block":
            draw_ice_block(canvas, self.x, self.y, self.width, self.height)
        else:
            # Fallback to rectangle for other types
            Color(*self.color)
            Rectangle(pos=(self.x, self.y), size=(self.width, self.height))

    def update(self):
        if self.melting:
            self.height -= self.melt_speed
            self.y += self.melt_speed
            if self.height <= 0:
                return True
        
        if self.type == "moving":
            self.x += self.move_speed * self.move_direction
            if self.x <= 0 or self.x + self.width >= WIDTH:
                self.move_direction *= -1
        
        if self.separation_cooldown > 0:
            self.separation_cooldown -= 1
        
        return False

    def collide(self, robot):
        return (robot.x < self.x + self.width and
                robot.x + robot.width > self.x and
                robot.y < self.y + self.height and
                robot.y + robot.height > self.y)

    def separate(self):
        if self.separation_cooldown == 0 and self.width > 20:
            self.separation_cooldown = 60
            new_width = self.width // 2
            new_obstacle = Obstacle(self.x + new_width, self.y, new_width, self.height, self.color, self.type)
            self.width = new_width
            return new_obstacle
        return None

class Slope(Obstacle):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height, BROWN, "slope")

    def draw(self, canvas):
        draw_slope(canvas, self.x, self.y, self.width, self.height)

    def collide(self, robot):
        if super().collide(robot):
            # Calculate the y-position on the slope
            slope = self.height / self.width
            relative_x = robot.x + robot.width - self.x
            y_on_slope = self.y + self.height - (slope * relative_x)
            
            if robot.y + robot.height > y_on_slope:
                robot.y = y_on_slope - robot.height
                robot.is_jumping = False
                robot.velocity_y = 0
                return True
        return False