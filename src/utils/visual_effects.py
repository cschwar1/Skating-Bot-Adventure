import random
from kivy.graphics import Color, Ellipse

class VisualEffects:
    @staticmethod
    def create_snowflake(canvas, x, y):
        with canvas:
            Color(1, 1, 1, 0.8)  # White, slightly transparent
            Ellipse(pos=(x, y), size=(5, 5))

    @staticmethod
    def create_star(canvas, x, y):
        with canvas:
            Color(1, 1, 0, 0.8)  # Yellow, slightly transparent
            for _ in range(5):
                Ellipse(pos=(x + random.randint(-10, 10), y + random.randint(-10, 10)), size=(3, 3))

    @staticmethod
    def create_leaf(canvas, x, y):
        with canvas:
            Color(0, 0.8, 0, 0.8)  # Green, slightly transparent
            Ellipse(pos=(x, y), size=(8, 4))

visual_effects = VisualEffects()