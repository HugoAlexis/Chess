from player import Player
from board import *
import pygame

class Game:
    """
        Control the game.
    """
    def __init__(self):
        """
            Create the new game: the board and the players, with
            the initial configuration of the board.
        """
        self.board = Board((10, 10))
        self.players = {'white': Player('white', self.board),
                        'black': Player('black', self.board),
                    }
        self.p_playing = 'white'

    def _change_p_playing(self):
        """
            Change the player who is playing.
        """
        if self.p_playing == 'white':
            self.p_playing = 'black'
        else:
            self.p_playing = 'white'

    def update(self):
        """
            Update the game every frame.
        """
        self.board.update()

    def process_events(self, type):
        """
            Process the events of the game.
        """
        if type == 'MOUSEBUTTONDOWN':
            pos = pygame.mouse.get_pos()
            ocuppied = self.board.ocuppied_cells(*self.players.values())
            player = self.players[self.p_playing]
            moved = player.control_click(pos, ocuppied)

            if moved:
                self._change_p_playing()

    def draw(self, screen):
        """
            Draw the board and all the game inside it.
        """
        self.board.draw(screen)
        for player in self.players.values():
            player.draw_pieces(screen)
        