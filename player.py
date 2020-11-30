from pygame.sprite import Group
from pieces import *
import numpy as np

class Player:
    """
        The player class, which have and control the
        pieces.
    """
    def __init__(self, color, board):
        self.board = board
        self.color = color
        self._create_pieces()
        

        self.selected_piece = None

    def _create_pieces(self):
        self.pieces = Group()
        self._create_pawns()
        self._create_main_pieces()

    def _create_pawns(self):
        if self.color == 'white':
            row = 6
        elif self.color == 'black':
            row = 1

        for i in range(8):
            pawn = Pawn(self.color, (i, row), self.board)
            self.pieces.add(pawn)

    def _create_main_pieces(self):
        if self.color == 'white':
            row = 7
            pieces = [Rook, Horse, Bishop, Queen, 
                      King, Bishop, Horse, Rook]
        elif self.color == 'black':
            row = 0
            pieces = [Rook, Horse, Bishop, King, 
                      Queen, Bishop, Horse, Rook]

        for i, piece in enumerate(pieces):
            pl_piece = piece(self.color, (i, row), self.board)
            self.pieces.add(pl_piece)

    def draw_pieces(self, screen):
        self.pieces.draw(screen)

    def control_click(self, pos, ocuppied):
        if self.selected_piece is None:
            for piece in self.pieces:
                if piece.rect.collidepoint(pos):
                    self.selected_piece = piece
                    self.selected_piece.selected = True
                    break

        elif self.selected_piece is not None:
            pos_i = (pos[0] - self.board.rect.x) // 60
            pos_j = (pos[1] - self.board.rect.y) // 60
            moved = self.selected_piece.move_piece(pos_i, pos_j, ocuppied)
            self.selected_piece.selected = False
            self.selected_piece = None

            return moved

    def ocuppied_cells(self):
        """
            Return a np.array representing the positions of the
            chess board, with 0 (if the cell is empty) or 1 (if
            some piece of the player is in that piece).
        """
        ocuppied = np.zeros((8, 8))
        for piece in self.pieces:
            i, j = piece.position 
            ocuppied[j, i] = piece.key

        return ocuppied