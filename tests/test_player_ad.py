from dilemma.player_ad import AlwaysDefectPlayer
from dilemma.player_rnd import RandomPlayer
from dilemma.game import Game


class TestAlwaysDefectPlayer(object):
    rounds = 5
    discount = 0.9
    game = Game(AlwaysDefectPlayer, RandomPlayer, rounds, discount)
    history = game.run()
    my_plays = history['RowAction'].tolist()
    for play in my_plays:
        assert play == 'D'
