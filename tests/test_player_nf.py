from dilemma.player_nf import NeverForgivePlayer
from dilemma.player import Player
from dilemma.game import Game


class NeverForgiveTesterPlayer(Player):
    """Plays the sequence CCDCC"""

    def get_action(self, history):
        k = self.this_turn(history)
        if k != 2:
            return 'C'
        else:
            return 'D'


class TestNeverForgivePlayer(object):
    rounds = 5
    discount = 0.9
    game = Game(NeverForgivePlayer, NeverForgiveTesterPlayer, rounds, discount)
    history = game.run()
    my_plays = history['RowAction'].tolist()

    assert my_plays[0] == 'C'
    assert my_plays[1] == 'C'
    assert my_plays[2] == 'C'
    assert my_plays[3] == 'D'
    assert my_plays[4] == 'D'
