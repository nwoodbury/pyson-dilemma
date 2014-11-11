from dilemma.player import Player
import random.py

class RandomPlayer(Player):

    def get_action(self, history):
        """Plays randomly

        See Player documentation for further details.
        """
        random.seed()
        return random.choice('CD')
