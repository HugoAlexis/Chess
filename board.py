import pygame
import numpy as np
from pygame.sprite import Sprite


class Board:

    def __init__(self, pos):
        self.image_orig = pygame.image.load('images/board480.png').\
                                 convert()
        self.image = self.image_orig.copy()
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def draw(self, surf):
        surf.blit(self.image, self.rect)

    def update(self):
        self.update_hover()

    def update_hover(self):
        mouse_pos = pygame.mouse.get_pos()
        self.image = self.image_orig.copy()
        if self.rect.collidepoint(mouse_pos):
            i = (mouse_pos[0] - self.rect.x) // 60
            j = (mouse_pos[1] - self.rect.y) // 60

            x_rect =60 * i 
            y_rect =60 * j

            pygame.draw.rect(self.image, (0, 255, 0),
                             (x_rect, y_rect, 60, 60), 3)

    def ocuppied_cells(self, player1, player2):
        occupied = player1.ocuppied_cells() +\
                   player2.ocuppied_cells()
        return occupied