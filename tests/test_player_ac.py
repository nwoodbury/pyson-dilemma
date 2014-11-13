from dilemma.player_ac import AlwaysCooperatePlayer
from dilemma.player_rnd import RandomPlayer
from dilemma.game import Game


class TestAlwaysCooperatePlayer(object):

    rounds = 5
    discount = 0.9
    game = Game(AlwaysCooperatePlayer, RandomPlayer, rounds, discount)
    history = game.run()
    my_plays = history['RowAction'].tolist()
    for play in my_plays:
        assert play == 'C'