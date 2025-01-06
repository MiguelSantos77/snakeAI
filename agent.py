from game import SnakeGame ,BLOCK_SIZE
import random

class SnakeAgent:
    def __init__(self):
        self.game = SnakeGame()
        self.epsilon = 1.0  
        self.gamma = 0.9  
        self.learning_rate = 0.01
        self.q_table = {} 
        self.record =0

    def get_state(self):
        head = self.game.snake[0]
        point_l = [head[0] - BLOCK_SIZE, head[1]]
        point_r = [head[0] + BLOCK_SIZE, head[1]]
        point_u = [head[0], head[1] - BLOCK_SIZE]
        point_d = [head[0], head[1] + BLOCK_SIZE]

        state = [
            self.game.is_collision(point_l),
            self.game.is_collision(point_r),
            self.game.is_collision(point_u),
            self.game.is_collision(point_d),
            self.game.food[0] < head[0], 
            self.game.food[0] > head[0], 
            self.game.food[1] < head[1], 
            self.game.food[1] > head[1]
        ]
        return tuple(state)

    def choose_action(self, state):
        if random.random() < self.epsilon:
            return random.choice(['UP', 'DOWN', 'LEFT', 'RIGHT'])
        return max(self.q_table.get(state, {}), key=lambda x: self.q_table[state].get(x, 0), default='UP')

    def train(self):
        state = self.get_state()
        action = self.choose_action(state)
        reward, game_over, score = self.game.play_step(action)
        next_state = self.get_state()

        if state not in self.q_table:
            self.q_table[state] = {}
        if action not in self.q_table[state]:
            self.q_table[state][action] = 0

        max_next = max(self.q_table.get(next_state, {}).values(), default=0)
        self.q_table[state][action] += self.learning_rate * (reward + self.gamma * max_next - self.q_table[state][action])

        if game_over:
            self.game.reset()

    def run(self):
        while True:
            self.train()
            if self.epsilon > 0.01:
                self.epsilon *= 0.995 

if __name__ == "__main__":
    agent = SnakeAgent()
    agent.run()
