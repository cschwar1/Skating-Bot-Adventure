import unittest
from kivy.tests.common import GraphicUnitTest
from src.game.game import Game
from src.utils.constants import WIDTH, HEIGHT

class TestGame(GraphicUnitTest):
    def setUp(self):
        super().setUp()
        self.game = Game()

    def test_game_initialization(self):
        self.assertIsNotNone(self.game.robot)
        self.assertEqual(self.game.current_level, 0)
        self.assertEqual(self.game.game_state, "MENU")

    def test_handle_touch(self):
        self.game.handle_touch(WIDTH // 2, HEIGHT // 2)
        self.assertEqual(self.game.game_state, "PLAYING")

    def test_update(self):
        self.game.game_state = "PLAYING"
        initial_score = self.game.robot.score
        self.game.update()
        self.assertGreater(self.game.robot.score, initial_score)

    def test_draw(self):
        self.game.draw(self._Canvas())  # Mock canvas for testing
        # Add assertions to check if draw methods were called

class _Canvas:
    def __init__(self):
        self.operations = []

    def add(self, instruction):
        self.operations.append(instruction)

if __name__ == '__main__':
    unittest.main()