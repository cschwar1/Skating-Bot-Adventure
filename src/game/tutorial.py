from kivy.graphics import Color, Rectangle
from kivy.core.text import Label as CoreLabel
from utils.constants import WIDTH, HEIGHT

class Tutorial:
    def __init__(self):
        self.steps = [
            "Welcome to Skating Bot Adventure!",
            "Use left and right arrow keys to move",
            "Press spacebar to jump",
            "Perform acrobatics by jumping on slopes",
            "Avoid obstacles and collect points",
            "Answer educational questions for bonus points",
            "Have fun and learn while playing!"
        ]
        self.current_step = 0
        self.font_size = 24

    def next_step(self):
        self.current_step = (self.current_step + 1) % len(self.steps)

    def draw(self, canvas):
        canvas.add(Color(0, 0, 0, 0.7))
        canvas.add(Rectangle(pos=(50, HEIGHT/2 - 100), size=(WIDTH - 100, 200)))
        canvas.add(Color(1, 1, 1, 1))

        step_label = CoreLabel(text=self.steps[self.current_step], font_size=self.font_size)
        step_label.refresh()
        texture = step_label.texture
        canvas.add(Rectangle(texture=texture, pos=(WIDTH/2 - texture.width/2, HEIGHT/2), size=texture.size))

        continue_label = CoreLabel(text="Tap to continue", font_size=self.font_size)
        continue_label.refresh()
        texture = continue_label.texture
        canvas.add(Rectangle(texture=texture, pos=(WIDTH/2 - texture.width/2, HEIGHT/2 - 50), size=texture.size))

tutorial = Tutorial()