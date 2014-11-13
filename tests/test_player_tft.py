from dilemma.player_tft import TitForTatPlayer
from dilemma.player import Player
from dilemma.game import Game


class TitForTatTesterPlayer(Player):
    """Plays the sequence DCCDD"""

    def get_action(self, history):
        k = self.this_turn(history)
        if k == 1 or k == 2:
            return 'C'
        else:
            return 'D'


class TestTitForTatPlayer(object):
    rounds = 5
    discount = 0.9
    game = Game(TitForTatPlayer, TitForTatTesterPlayer, rounds, discount)
    history = game.run()
    my_plays = history['RowAction'].tolist()

    assert my_plays[0] == 'C'
    assert my_plays[1] == 'D'
    assert my_plays[2] == 'C'
    assert my_plays[3] == 'C'
    assert my_plays[4] == 'D'


