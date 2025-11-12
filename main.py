import pygame
import sys
from game import Game
from colors import Colors

# Constants
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 620
FPS = 60
GAME_UPDATE_INTERVAL = 200  # milliseconds

SCORE_RECT = pygame.Rect(320, 55, 170, 60)
NEXT_RECT = pygame.Rect(320, 215, 170, 180)

def main():
    pygame.init()
    
    # Fonts and surfaces
    title_font = pygame.font.Font(None, 40)
    score_surface = title_font.render("Score", True, Colors.white)
    next_surface = title_font.render("Next", True, Colors.white)
    game_over_surface = title_font.render("GAME OVER", True, Colors.white)
    
    # Screen and clock
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Python Tetris")
    clock = pygame.time.Clock()
    
    # Game instance
    game = Game()
    
    # Custom event for game updates
    GAME_UPDATE = pygame.USEREVENT
    pygame.time.set_timer(GAME_UPDATE, GAME_UPDATE_INTERVAL)
    
    while True:
        handle_events(game, GAME_UPDATE)
        draw(screen, game, title_font, score_surface, next_surface, game_over_surface)
        clock.tick(FPS)

def handle_events(game, GAME_UPDATE):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if game.game_over:
                game.game_over = False
                game.reset()
            elif not game.game_over:
                if event.key == pygame.K_LEFT:
                    game.move_left()
                elif event.key == pygame.K_RIGHT:
                    game.move_right()
                elif event.key == pygame.K_DOWN:
                    game.move_down()
                    game.update_score(0, 1)
                elif event.key == pygame.K_UP:
                    game.rotate()
        elif event.type == GAME_UPDATE and not game.game_over:
            game.move_down()

def draw(screen, game, title_font, score_surface, next_surface, game_over_surface):
    screen.fill(Colors.dark_blue)
    
    # Draw labels
    screen.blit(score_surface, (365, 20))
    screen.blit(next_surface, (375, 180))
    
    # Draw game over if applicable
    if game.game_over:
        screen.blit(game_over_surface, (320, 450))
    
    # Draw score rectangle and value
    pygame.draw.rect(screen, Colors.light_blue, SCORE_RECT, 0, 10)
    score_value_surface = title_font.render(str(game.score), True, Colors.white)
    screen.blit(score_value_surface, score_value_surface.get_rect(center=SCORE_RECT.center))
    
    # Draw next rectangle
    pygame.draw.rect(screen, Colors.light_blue, NEXT_RECT, 0, 10)
    
    # Draw the game
    game.draw(screen)
    
    pygame.display.update()

if __name__ == "__main__":
    main()
