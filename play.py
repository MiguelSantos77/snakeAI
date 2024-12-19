from game import SnakeGame
import pygame

def main():
    game = SnakeGame()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        action = None
        if keys[pygame.K_UP]:
            action = 'UP'
        elif keys[pygame.K_DOWN]:
            action = 'DOWN'
        elif keys[pygame.K_LEFT]:
            action = 'LEFT'
        elif keys[pygame.K_RIGHT]:
            action = 'RIGHT'

        reward, game_over, score = game.play_step(action)

if __name__ == "__main__":
    main()
