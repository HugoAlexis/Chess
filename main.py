import pygame
from board import Board
from player import Player
from pieces import *
import sys

pygame.init
from board import *

screen = pygame.display.set_mode((1000, 800))
pygame.display.set_caption('Chess')

board = Board((100, 10))
mouse = MouseMarker(screen, board)
player_white = Player('white', board)
player_black = Player('black', board)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            player_white.control_click(pos)



    board.update()
    mouse.update()

    screen.fill((0, 0, 0))
    board.draw(screen)
    mouse.draw(screen)
    player_white.draw_pieces(screen)
    player_black.draw_pieces(screen)
    pygame.display.flip()