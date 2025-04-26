class ScoreTracker:
    def __init__(self):
        self.score = 0

    def increase_score(self, points):
        self.score += points
        print(f"Score increased by {points}. Current score: {self.score}")

    def decrease_score(self, points):
        self.score -= points
        print(f"Score decreased by {points}. Current score: {self.score}")

    def get_score(self):
        return self.score

    def reset_score(self):
        self.score = 0
        print("Score has been reset.")  

    def display_score(self):
        print(f"Current score: {self.score}")
    def save_score(self, filename):             
        with open(filename, 'w') as file:
            file.write(str(self.score))
        print(f"Score saved to {filename}")                             
    def load_score(self, filename):
        try:
            with open(filename, 'r') as file:
                self.score = int(file.read())
            print(f"Score loaded from {filename}. Current score: {self.score}")
        except FileNotFoundError:       
            print(f"File {filename} not found. Score not loaded.")
        except ValueError:
            print(f"Invalid data in {filename}. Score not loaded.")