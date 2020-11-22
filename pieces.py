from pygame.sprite import Sprite
import pygame

class Horse(Sprite):

    def __init__(self, i, j, color, board):
        """
            Create the sprite for the horse.
        """
        super().__init__()
        self.color = color
        self.board = board
        self.i = i 
        self.j = j

        self.image_orig = pygame.image.load(f'images/horse_{color}.png')\
                     .convert_alpha()
        self.image = self.image_orig.copy()
        self.rect = self.image.get_rect()
        self.pos_horse()

        self.selected = False

    def pos_horse(self):
        """
        Finde the coordinates of the horse in the window, 
        using its (i, j) position in the board.
        """
        x = self.board.rect.x + 60 * self.i 
        y = self.board.rect.y + 60 * self.j
        self.rect.x = x
        self.rect.y = y

    def move_horse(self, new_i, new_j):
        move = [abs(new_i - self.i), 
                abs(new_j - self.j)]

        # Validate the move
        if 2 in move and 1 in move and 0 <= new_i <=7 and 0 <= new_j <=7:
            self.i = new_i
            self.j = new_j
            self.pos_horse()

        self.selected = False

    def update(self):
        if self.selected:
            pygame.draw.rect(self.image, (0, 0, 255), (0, 0, 60, 60), 5)
        else:
            self.image = self.image_orig.copy()
        
    def draw(self, screen):
        screen.blit(self.image, self.rect)
