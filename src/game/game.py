# ... (previous imports)
from utils.progress_tracker import progress_tracker

class Game:
    # ... (previous methods)

    def handle_educational_input(self, x, y):
        if self.educational_challenge:
            correct_answer = self.educational_challenge.get("answer", "").lower()
            if self.answer_input.lower() == correct_answer:
                score = 50
                self.robot.score += score
                progress_tracker.update_progress(score=score, challenge_completed=True)
                audio_manager.play_correct_answer_sound()
                self.educational_challenge = None
                self.answer_input = ""
            else:
                audio_manager.play_wrong_answer_sound()

    def next_level(self):
        self.current_level = (self.current_level + 1) % len(self.levels)
        self.robot.x = 50
        self.robot.y = HEIGHT - 100
        progress_tracker.update_progress(level_completed=True)

    # ... (other methods)

    def draw_hud(self, canvas):
        # ... (previous HUD drawing)

        # Draw progress information
        progress_label = CoreLabel(text=f"Levels: {progress_tracker.progress['levels_completed']} | Challenges: {progress_tracker.progress['educational_challenges_completed']}", font_size=self.font_size)
        progress_label.refresh()
        texture = progress_label.texture
        canvas.add(Rectangle(texture=texture, pos=(WIDTH/2 - texture.width/2, HEIGHT - 40), size=texture.size))

    # ... (other methods)