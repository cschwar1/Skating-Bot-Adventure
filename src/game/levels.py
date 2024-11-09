import random
from game.obstacles import Obstacle, Slope
from utils.constants import WIDTH, HEIGHT, RED, GREEN, BLUE, YELLOW

class Level:
    def __init__(self, obstacles, theme):
        self.obstacles = obstacles
        self.theme = theme

    def update(self):
        for obstacle in self.obstacles[:]:
            if obstacle.update():
                self.obstacles.remove(obstacle)
            elif random.random() < 0.01:  # 1% chance each frame
                new_obstacle = obstacle.separate()
                if new_obstacle:
                    self.obstacles.append(new_obstacle)

    def draw(self, canvas):
        for obstacle in self.obstacles:
            obstacle.draw(canvas)

def create_levels():
    return [
        Level([
            Obstacle(200, HEIGHT - 150, 100, 50, RED, "ice_block"),
            Obstacle(500, HEIGHT - 200, 150, 100, GREEN, "snowball"),
            Slope(350, HEIGHT - 250, 200, 100)
        ], "winter_wonderland"),
        Level([
            Obstacle(100, HEIGHT - 200, 150, 100, BLUE, "crystal"),
            Obstacle(400, HEIGHT - 150, 100, 50, YELLOW, "star"),
            Slope(600, HEIGHT - 300, 150, 150),
            Obstacle(300, HEIGHT - 100, 50, 50, GREEN, "moving")
        ], "space_adventure"),
        Level([
            Obstacle(50, HEIGHT - 150, 75, 75, GREEN, "leaf"),
            Obstacle(200, HEIGHT - 200, 100, 100, BROWN, "log"),
            Slope(400, HEIGHT - 250, 250, 150),
            Obstacle(700, HEIGHT - 175, 50, 100, RED, "moving")
        ], "forest_journey"),
        # Add more levels with different themes
    ]