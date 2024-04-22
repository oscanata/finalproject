'''I haven't yet implemented to the code to end the game when a bomb is clicked or when all the non-bomb tiles are revealed. 
I also don't yet have programming to blow up an entire cave of non-mine-adjacent tiles at once. 
I will complete this in the coming week'''

import pygame
import numpy as np
import random
import sys


pygame.init()

#VAIRABLES
TILE_SIZE = 40
GRID_SIZE = 10
BOMBS_NUMBER = 15
WIDTH = HEIGHT = TILE_SIZE * GRID_SIZE
WHITE = (255, 255, 255)
GRAY = (192, 192, 192)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
FLAG_COLOR = (255, 255, 0)

#DISPLAY
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Minesweeper")
font = pygame.font.Font(None, 30)
clock = pygame.time.Clock()

class Tile:
    def __init__(self, is_bomb=False):
        self.is_hidden = True
        self.is_bomb = is_bomb
        self.neighbor_bombs = 0
        self.is_flagged = False

class Board:
    def __init__(self):
        self.tiles = np.array([[Tile() for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)])
        self.first_click = True

    def place_bombs(self, x, y):
        placed_bombs = 0
        while placed_bombs < BOMBS_NUMBER:
            bx, by = random.randint(0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - 1)
            if not self.tiles[by][bx].is_bomb and (bx, by) != (x, y):
                self.tiles[by][bx].is_bomb = True
                placed_bombs += 1
                for dx in [-1, 0, 1]:
                    for dy in [-1, 0, 1]:
                        nx, ny = bx + dx, by + dy
                        if 0 <= nx < GRID_SIZE and 0 <= ny < GRID_SIZE:
                            self.tiles[ny][nx].neighbor_bombs += 1

    def draw(self):
        for y in range(GRID_SIZE):
            for x in range(GRID_SIZE):
                rect = pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE)
                tile = self.tiles[y][x]
                if tile.is_hidden:
                    pygame.draw.rect(screen, GRAY, rect)
                    if tile.is_flagged:
                        pygame.draw.circle(screen, FLAG_COLOR, rect.center, TILE_SIZE // 4)
                else:
                    if tile.is_bomb:
                        pygame.draw.ellipse(screen, BLACK, rect)
                    else:
                        pygame.draw.rect(screen, WHITE, rect)
                        if tile.neighbor_bombs > 0:
                            text = font.render(str(tile.neighbor_bombs), True, BLACK)
                            screen.blit(text, text.get_rect(center=rect.center))
                pygame.draw.rect(screen, BLACK, rect, 1)  

def main():
    board = Board()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos[0] // TILE_SIZE, event.pos[1] // TILE_SIZE
                if event.button == 1:  
                    if board.first_click:
                        board.place_bombs(x, y)
                        board.first_click = False
                    board.tiles[y][x].is_hidden = False
                elif event.button == 3:  
                    if board.tiles[y][x].is_hidden:
                        board.tiles[y][x].is_flagged = not board.tiles[y][x].is_flagged

        screen.fill(BLACK)
        board.draw()
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
