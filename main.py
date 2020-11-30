import pygame
from game import Game
from board import *
import sys

pygame.init()
screen = pygame.display.set_mode((1000, 800))
pygame.display.set_caption('Chess')

game = Game()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            game.process_events('MOUSEBUTTONDOWN')

    game.update()
    screen.fill((0, 0, 0))
    game.draw(screen)
    pygame.display.flip()