import pygame
import numpy as np
from pygame.sprite import Sprite


class MouseMarker():
    """
    Controlls the markers according tho the mouse
    position.
    """
    def __init__(self, screen, board):

        self.board = board
        self.screen = screen

        self.image = pygame.Surface((60, 60))
        self.image.fill((0, 0, 0))
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        
    def update(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.board.rect.collidepoint(mouse_pos):
            self.mouse_in_board(mouse_pos)
        else: 
            self.image.fill((0, 0, 0))

    def mouse_in_board(self, mouse_pos):
        x = (mouse_pos[0] - self.board.rect.x) // 60 
        y = (mouse_pos[1] - self.board.rect.y) //60

        x *= 60
        y *= 60

        self.image.fill((0, 255, 0))
        self.rect.x = self.board.rect.x + x
        self.rect.y = self.board.rect.y + y
        pygame.draw.rect(self.image, (0, 0, 0), (5, 5, 50, 50))


    def draw(self, screen):
        screen.blit(self.image, self.rect)


class Board(Sprite):
    """
    Represents the complete board.
    """
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.image.load('images/board480.png')
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]

        self.squares = np.zeros((8, 8))

    def draw(self, surf):
        surf.blit(self.image, self.rect)

