import json

class ProgressTracker:
    def __init__(self):
        self.progress = {
            "levels_completed": 0,
            "total_score": 0,
            "educational_challenges_completed": 0,
            "achievements": set()
        }
        self.load_progress()

    def update_progress(self, level_completed=False, score=0, challenge_completed=False):
        if level_completed:
            self.progress["levels_completed"] += 1
        self.progress["total_score"] += score
        if challenge_completed:
            self.progress["educational_challenges_completed"] += 1
        self.check_achievements()
        self.save_progress()

    def check_achievements(self):
        if self.progress["levels_completed"] >= 5:
            self.progress["achievements"].add("Level Master")
        if self.progress["total_score"] >= 1000:
            self.progress["achievements"].add("Point Prodigy")
        if self.progress["educational_challenges_completed"] >= 10:
            self.progress["achievements"].add("Education Expert")

    def save_progress(self):
        with open("progress.json", "w") as f:
            json.dump(self.progress, f, default=lambda x: list(x) if isinstance(x, set) else x)

    def load_progress(self):
        try:
            with open("progress.json", "r") as f:
                loaded_progress = json.load(f)
                loaded_progress["achievements"] = set(loaded_progress["achievements"])
                self.progress = loaded_progress
        except FileNotFoundError:
            pass  # Use default progress if file doesn't exist

progress_tracker = ProgressTracker()