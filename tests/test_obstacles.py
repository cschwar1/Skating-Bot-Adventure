import unittest
from src.game.obstacles import Obstacle, Slope
from src.game.robot import Robot
from src.utils.constants import WIDTH, HEIGHT, RED

class TestObstacle(unittest.TestCase):
    def setUp(self):
        self.obstacle = Obstacle(100, HEIGHT - 50, 50, 50, RED)
        self.robot = Robot(50, HEIGHT - 100)

    def test_initial_position(self):
        self.assertEqual(self.obstacle.x, 100)
        self.assertEqual(self.obstacle.y, HEIGHT - 50)

    def test_collision(self):
        self.assertFalse(self.obstacle.collide(self.robot))
        self.robot.x = 90
        self.assertTrue(self.obstacle.collide(self.robot))

    def test_update(self):
        self.obstacle.melting = True
        initial_height = self.obstacle.height
        self.obstacle.update()
        self.assertTrue(self.obstacle.height < initial_height)

    def test_separate(self):
        new_obstacle = self.obstacle.separate()
        self.assertIsNotNone(new_obstacle)
        self.assertEqual(self.obstacle.width, new_obstacle.width)

class TestSlope(unittest.TestCase):
    def setUp(self):
        self.slope = Slope(100, HEIGHT - 100, 100, 100)
        self.robot = Robot(50, HEIGHT - 100)

    def test_collision(self):
        self.assertFalse(self.slope.collide(self.robot))
        self.robot.x = 90
        self.robot.y = HEIGHT - 50
        self.assertTrue(self.slope.collide(self.robot))

if __name__ == '__main__':
    unittest.main()