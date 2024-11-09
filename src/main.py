from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.clock import Clock
from game.game import Game
from utils.audio import audio_manager

class SkatingBotGame(Widget):
    def __init__(self, **kwargs):
        super(SkatingBotGame, self).__init__(**kwargs)
        self.game = Game()
        Clock.schedule_interval(self.update, 1.0 / 60.0)
        self._keyboard = Window.request_keyboard(self._on_keyboard_closed, self)
        self._keyboard.bind(on_key_down=self._on_key_down)
        self._keyboard.bind(on_key_up=self._on_key_up)
        self.pressed_keys = set()
        audio_manager.play_background_music()

    def update(self, dt):
        self.game.update(dt, self.pressed_keys)
        self.canvas.clear()
        with self.canvas:
            self.game.draw()

    def on_touch_down(self, touch):
        self.game.handle_touch(touch.x, touch.y)

    def on_touch_move(self, touch):
        self.game.handle_touch_move(touch.x, touch.y)

    def _on_keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self._on_key_down)
        self._keyboard.unbind(on_key_up=self._on_key_up)
        self._keyboard = None

    def _on_key_down(self, keyboard, keycode, text, modifiers):
        self.pressed_keys.add(keycode[1])

    def _on_key_up(self, keyboard, keycode):
        self.pressed_keys.discard(keycode[1])

class SkatingBotApp(App):
    def build(self):
        game = SkatingBotGame()
        Window.size = (800, 600)
        return game

    def on_stop(self):
        audio_manager.stop_all()

if __name__ == '__main__':
    SkatingBotApp().run()