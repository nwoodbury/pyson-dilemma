from dilemma.player_tf2t import TitFor2TatsPlayer
from dilemma.player import Player
from dilemma.game import Game


class TitFor2TatsTesterPlayer(Player):
    """Plays the sequence DCCDDCCC"""

    def get_action(self, history):
        k = self.this_turn(history)
        if k == 0 or k == 3 or k == 4:
            return 'D'
        else:
            return 'C'


class TestTitFor2TatsPlayer(object):
    rounds = 8
    discount = 0.9
    game = Game(TitFor2TatsPlayer, TitFor2TatsTesterPlayer, rounds, discount)
    history = game.run()
    my_plays = history['RowAction'].tolist()
    for k in range(0, rounds):
        if k != 5:
            assert my_plays[k] == 'C'
        else:
            assert my_plays[k] == 'D'

