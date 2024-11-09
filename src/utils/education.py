import random

class EducationManager:
    def __init__(self):
        self.math_problems = [
            {"question": "What is 5 + 3?", "answer": "8"},
            {"question": "What is 10 - 4?", "answer": "6"},
            {"question": "What is 2 x 6?", "answer": "12"},
            {"question": "What is 15 ÷ 3?", "answer": "5"},
            {"question": "What is 7 + 8?", "answer": "15"},
            {"question": "What is 20 - 7?", "answer": "13"},
            {"question": "What is 4 x 5?", "answer": "20"},
            {"question": "What is 18 ÷ 2?", "answer": "9"},
        ]
        
        self.spelling_challenges = [
            {"word": "winter", "hint": "The cold season"},
            {"word": "skate", "hint": "To glide on ice"},
            {"word": "robot", "hint": "A machine that can move and do tasks"},
            {"word": "snow", "hint": "White flakes that fall in winter"},
            {"word": "ice", "hint": "Frozen water"},
            {"word": "cold", "hint": "The opposite of hot"},
            {"word": "freeze", "hint": "To turn into ice"},
            {"word": "sledge", "hint": "A vehicle for sliding on snow"},
        ]
        
        self.science_questions = [
            {"question": "What is the largest planet in our solar system?", "answer": "Jupiter"},
            {"question": "What is the process by which plants make their own food?", "answer": "Photosynthesis"},
            {"question": "What is the hardest natural substance on Earth?", "answer": "Diamond"},
            {"question": "What is the boiling point of water in degrees Celsius?", "answer": "100"},
        ]
        
        self.geography_questions = [
            {"question": "What is the largest continent?", "answer": "Asia"},
            {"question": "What is the longest river in the world?", "answer": "Nile"},
            {"question": "What is the capital of France?", "answer": "Paris"},
            {"question": "Which country is known as the Land of the Rising Sun?", "answer": "Japan"},
        ]
        
        self.fun_facts = [
            "Did you know that no two snowflakes are exactly alike?",
            "The first ice skates were made from animal bones!",
            "Robots can be programmed to do many different tasks.",
            "Some robots are so small they can't be seen without a microscope!",
            "The coldest temperature ever recorded on Earth was -128.6°F (-89.2°C) in Antarctica!",
            "The largest snowflake ever recorded was 15 inches wide and 8 inches thick!",
            "The word 'robot' comes from the Czech word 'robota', which means 'forced labor'.",
            "Some robots can perform surgery with more precision than human doctors!",
        ]

    def get_random_challenge(self):
        challenge_type = random.choice(["math", "spelling", "science", "geography"])
        if challenge_type == "math":
            return random.choice(self.math_problems)
        elif challenge_type == "spelling":
            return random.choice(self.spelling_challenges)
        elif challenge_type == "science":
            return random.choice(self.science_questions)
        else:
            return random.choice(self.geography_questions)

    def get_random_fun_fact(self):
        return random.choice(self.fun_facts)

education_manager = EducationManager()