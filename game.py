import pygame
import random

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
BLOCK_SIZE = 20
FPS = 150

class SnakeGame:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Snake AI")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont('arial', 20) 
        self.record = 0
        self.reset()

    def reset(self):
        self.snake = [[BLOCK_SIZE * 10, BLOCK_SIZE * 10], [BLOCK_SIZE * 4, BLOCK_SIZE * 5], [BLOCK_SIZE * 3, BLOCK_SIZE * 5]]
        self.direction = 'RIGHT'
        self.change_to = self.direction
        self.food = self.spawn_food()
        self.score = 0

    def spawn_food(self):
        while True:
            food = [
                random.randrange(0, SCREEN_WIDTH // BLOCK_SIZE) * BLOCK_SIZE,
                random.randrange(0, SCREEN_HEIGHT // BLOCK_SIZE) * BLOCK_SIZE
            ]
            if food not in self.snake:
                return food

    def is_collision(self, point=None):
        if point is None:
            point = self.snake[0]
        if point[0] < 0 or point[0] >= SCREEN_WIDTH or point[1] < 0 or point[1] >= SCREEN_HEIGHT:
            return True
        if point in self.snake[1:]:
            return True
        return False

    def move(self):
        x, y = self.snake[0]
        if self.direction == 'UP':
            y -= BLOCK_SIZE
        elif self.direction == 'DOWN':
            y += BLOCK_SIZE
        elif self.direction == 'LEFT':
            x -= BLOCK_SIZE
        elif self.direction == 'RIGHT':
            x += BLOCK_SIZE
        new_head = [x, y]

        
        if new_head == self.food:
            self.snake.insert(0, new_head)
            self.food = self.spawn_food()
            self.score += 1
            if self.score > self.record:
                self.record = self.score
            return True
        else:
            self.snake.insert(0, new_head)
            self.snake.pop()
            return False

    def render(self):
        self.screen.fill((0, 0, 0))
        for block in self.snake:
            pygame.draw.rect(self.screen, (0, 255, 0), pygame.Rect(block[0], block[1], BLOCK_SIZE, BLOCK_SIZE))
        pygame.draw.rect(self.screen, (255, 0, 0), pygame.Rect(self.food[0], self.food[1], BLOCK_SIZE, BLOCK_SIZE))
        
        score_text = self.font.render(f"Score: {self.score}", True, (255, 255, 0))
        record_text = self.font.render(f"Record: {self.record}", True, (255, 255, 0))
        self.screen.blit(score_text, (10, 10)) 
        self.screen.blit(record_text, (SCREEN_WIDTH-140, 10)) 

        pygame.display.flip()

    def play_step(self, action):
        if action == 'UP' and self.direction != 'DOWN':
            self.direction = 'UP'
        elif action == 'DOWN' and self.direction != 'UP':
            self.direction = 'DOWN'
        elif action == 'LEFT' and self.direction != 'RIGHT':
            self.direction = 'LEFT'
        elif action == 'RIGHT' and self.direction != 'LEFT':
            self.direction = 'RIGHT'

        reward = 0
        game_over = False
        ate_food = self.move()
        if ate_food:
            reward = 10
        if self.is_collision():
            reward = -10
            game_over = True
            self.reset()

        self.render()
        self.clock.tick(FPS)
        return reward, game_over, self.score
