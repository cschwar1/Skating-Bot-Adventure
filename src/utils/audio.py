from kivy.core.audio import SoundLoader

class AudioManager:
    def __init__(self):
        self.background_music = SoundLoader.load('src/assets/sounds/background_music.mp3')
        self.jump_sound = SoundLoader.load('src/assets/sounds/jump.wav')
        self.collision_sound = SoundLoader.load('src/assets/sounds/collision.wav')
        self.acrobatic_sound = SoundLoader.load('src/assets/sounds/acrobatic.wav')
        
        self.sounds = [self.background_music, self.jump_sound, self.collision_sound, self.acrobatic_sound]
        self.volume = 1.0

    def play_background_music(self):
        if self.background_music:
            self.background_music.loop = True
            self.background_music.play()

    def play_jump_sound(self):
        if self.jump_sound:
            self.jump_sound.play()

    def play_collision_sound(self):
        if self.collision_sound:
            self.collision_sound.play()

    def play_acrobatic_sound(self):
        if self.acrobatic_sound:
            self.acrobatic_sound.play()

    def set_volume(self, volume):
        self.volume = max(0, min(1, volume))
        for sound in self.sounds:
            if sound:
                sound.volume = self.volume

    def stop_all(self):
        for sound in self.sounds:
            if sound:
                sound.stop()

audio_manager = AudioManager()