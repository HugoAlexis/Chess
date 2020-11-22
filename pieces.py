from abc import ABC, abstractmethod
from pygame.sprite import Sprite
import pygame


class Piece(Sprite, ABC):

    def __init__(self, piece, color, pos, board):
        """
            Create the sprite for the piece and the color
            in the parameters, and place it in the position
            pos in the board.
            :param piece: str
            :param color: str
            :param pos: tuple(str, str)
        """
        super().__init__()
        self.board = board
        self.color = color
        self.board = board
        self.i = pos[0]
        self.j = pos[1]

        self.image_orig = pygame.image.load(f'images/{piece}_{color}.png')\
                                            .convert_alpha()

        self.image = self.image_orig.copy()
        self.rect = self.image.get_rect()
        self._set_position()

        # If the move is selected by the player to make the move.
        self._selected = False

    @property
    def selected(self):
        """
            Setter for the selected attribute.
        """
        return self._selected

    @selected.setter
    def selected(self, value):
        """
        Setter for the selected attribute. If the piece is selected, 
        create a blue box around the piece to show the player that
        the piece is selected.
        """
        if value == True:
            pygame.draw.rect(self.image, (0, 0, 255), (0, 0, 60, 60), 5)
        elif value == False:
            self.image = self.image_orig.copy()
        else:
            raise ValueError('Selected most be a bool value.')
        
        self._selected = value

    def _set_position(self):
        """
            Set the coordinates of the horse in the window, 
            corresponding to its position (i, j) in the board.
        """
        x = self.board.rect.x + (60 * self.i)
        y = self.board.rect.y + (60 * self.j)
        self.rect.x = x
        self.rect.y = y

    def draw(self, screen):
        """
        Draw the piece on the screen.
        """
        screen.blit(self.image, self.rect)

    def _val_in_board(self, new_i, new_j):
        """
        Check if the new position of the piece is still inside
        the board.
        """
        if (0 <= new_i <= 7) and (0 <= new_j <= 7):
            return True

    @abstractmethod
    def _val_piece_move(self, move):
        """
            Check if the move of the piece is correct, according to 
            the type of piece.
        """
        pass

    def move_piece(self, new_i, new_j):
        """
            Check if the desired move of the piece is valid.
            If so, move the piece to the new position, otherwise
            cancel the move.
        """
        move = [new_i - self.i,
                new_j - self.j]

        if self._val_piece_move(move) and self._val_in_board(new_i, new_j):
            self.i = new_i
            self.j = new_j
            self._set_position()

        self.selected = False


class Horse(Piece):

    def __init__(self, color, pos, board):
        super().__init__('horse', color, pos, board)

    def _val_piece_move(self, move):
        """
            Check if the move of the piece is correct, according to 
            the type of piece.
        """
        move = [abs(move[0]), abs(move[1])]
        if (2 in move) and (1 in move):
            return True


class Pawn(Piece):

    def __init__(self, color, pos, board):
        super().__init__('pawn', color, pos, board)

    def _val_piece_move(self, move):
        """
            Check if the move of the piece is correct, according to 
            the type of piece.
        """
        if abs(move[0]) == abs(move[1]):
            return True