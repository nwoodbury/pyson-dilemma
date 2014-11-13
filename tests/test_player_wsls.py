from dilemma.player_wsls import WinStayLoseShiftPlayer
from dilemma.player import Player
from dilemma.game import Game


class WinStayLoseShiftTesterPlayer(Player):
    """Plays the sequence DDCCDD"""

    def get_action(self, history):
        k = self.this_turn(history)
        if k == 2 or k == 3:
            return 'C'
        else:
            return 'D'


class TestWinStayLoseShiftPlayer(object):
    rounds = 6
    discount = 0.9
    game = Game(WinStayLoseShiftPlayer, WinStayLoseShiftTesterPlayer, rounds, discount)
    history = game.run()
    my_plays = history['RowAction'].tolist()

    assert my_plays[0] == 'C'
    assert my_plays[1] == 'D'
    assert my_plays[2] == 'C'
    assert my_plays[3] == 'C'
    assert my_plays[4] == 'C'
    assert my_plays[5] == 'D'

