import tkinter as tk
from agent import SnakeAgent
import pickle
import threading


class TK:
    
    def __init__(self, root):
        self.agent = SnakeAgent()

        self.root = root
        self.root.title("Snake AI Interface")

        self.start_button = tk.Button(root, text="Start Training", command=self.start_training)
        self.start_button.pack(pady=10)

        self.save_button = tk.Button(root, text="Save QTable", command=self.save_q_table)
        self.save_button.pack(pady=10)

        self.load_button = tk.Button(root, text="Load QTable", command=self.load_q_table)
        self.load_button.pack(pady=10)

        self.reset_button = tk.Button(root, text="Reset", command=self.reset_agent)
        self.reset_button.pack(pady=10)

        self.plot_button = tk.Button(root, text="Show Learning Grath", command=self.plot_progress)
        self.plot_button.pack(pady=10)
        


    def start_training(self):
        training_thread = threading.Thread(target=self.agent.run)
        training_thread.daemon = True
        training_thread.start()


    def save_q_table(self):
        with open("q_table.pkl", "wb") as f:
            pickle.dump(self.agent.q_table, f)
        print("Q_table saved")

    def load_q_table(self):
        try:
            with open("q_table.pkl", "rb") as f:
                self.agent.q_table = pickle.load(f)
                self.agent.game.reset()

            print("Q_table loaded")
        except FileNotFoundError:
            print("Q_table not found")

    def reset_agent(self):
        self.agent.q_table = {}
        self.agent.game.reset()


    def plot_progress(self):
        self.agent.game.learning_tracker.plot_progress()
        


if __name__ == "__main__":
    root = tk.Tk()
    app = TK(root)
    root.mainloop()
