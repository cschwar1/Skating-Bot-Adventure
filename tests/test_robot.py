import unittest
from src.game.robot import Robot
from src.utils.constants import WIDTH, HEIGHT

class TestRobot(unittest.TestCase):
    def setUp(self):
        self.robot = Robot(50, HEIGHT - 100)

    def test_initial_position(self):
        self.assertEqual(self.robot.x, 50)
        self.assertEqual(self.robot.y, HEIGHT - 100)

    def test_move(self):
        initial_x = self.robot.x
        self.robot.move(1)
        self.assertTrue(self.robot.x > initial_x)
        
        self.robot.move(-1)
        self.assertEqual(self.robot.x, initial_x)

    def test_jump(self):
        initial_y = self.robot.y
        self.robot.jump()
        self.assertTrue(self.robot.is_jumping)
        self.assertTrue(self.robot.velocity_y < 0)

    def test_perform_acrobatics(self):
        initial_score = self.robot.score
        self.robot.is_jumping = True
        self.robot.perform_acrobatics()
        self.assertTrue(self.robot.score > initial_score)
        self.assertEqual(self.robot.acrobatic_state, 1)

    def test_update(self):
        self.robot.jump()
        initial_y = self.robot.y
        self.robot.update([])
        self.assertTrue(self.robot.y < initial_y)

if __name__ == '__main__':
    unittest.main()