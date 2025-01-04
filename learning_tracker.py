import matplotlib.pyplot as plt

class LearningTracker:
    def __init__(self):
        self.scores = []  
        self.attempts = []  
        self.current_attempt = 0 

    def record_score(self, score):
        self.current_attempt += 1
        self.scores.append(score)
        self.attempts.append(self.current_attempt)

    def plot_progress(self):
        if not self.scores:
            return

        plt.figure(figsize=(10, 6) )
        plt.plot(self.attempts, self.scores, marker='o',linestyle='-', label="Score")
        plt.title("Learning Progress")
        plt.xlabel("Attempt")
        plt.ylabel("Score")
        plt.legend()
        plt.grid(True)
        plt.show()
