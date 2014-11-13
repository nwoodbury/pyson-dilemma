from dilemma.player_pavlov import PavlovPlayer
from dilemma.player import Player
from dilemma.game import Game


class PavlovTesterPlayer(Player):
    """Plays the sequence DDCDDD"""

    def get_action(self, history):
        k = self.this_turn(history)
        if k != 2:
            return 'D'
        else:
            return 'C'


class TestPavlovPlayer(object):
    rounds = 6
    discount = 0.9
    game = Game(PavlovPlayer, PavlovTesterPlayer, rounds, discount)
    history = game.run()
    my_plays = history['RowAction'].tolist()

    assert my_plays[0] == 'C'
    assert my_plays[1] == 'D'
    assert my_plays[2] == 'C'
    assert my_plays[3] == 'C'
    assert my_plays[4] == 'D'
    assert my_plays[5] == 'C'
