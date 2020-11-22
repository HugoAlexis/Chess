import pygame
from board import Board
from pieces import *
import sys

pygame.init
from board import *

screen = pygame.display.set_mode((1000, 800))
pygame.display.set_caption('Chess')

board = Board((100, 10))
mouse = MouseMarker(screen, board)
horse = Horse(1, 7, 'black', board)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            pos_i = (pos[0] - board.rect.x) // 60
            pos_j = (pos[1] - board.rect.y) // 60
            print(pos_i, pos_j)
            if horse.selected:
                horse.move_horse(pos_i, pos_j)
            elif horse.rect.collidepoint(pos):
                horse.selected = True

    board.update()
    mouse.update()
    horse.update()

    screen.fill((0, 0, 0))
    board.draw(screen)
    mouse.draw(screen)
    horse.draw(screen)
    pygame.display.flip()