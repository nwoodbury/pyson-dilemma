from dilemma.player_rnd import RandomPlayer
from dilemma.player_ac import AlwaysCooperatePlayer
from dilemma.game import Game


class TestPavlovPlayer(object):
    rounds = 6
    discount = 0.9
    game = Game(RandomPlayer, AlwaysCooperatePlayer, rounds, discount)
    history = game.run()
    prev_plays = history['RowAction'].tolist()

    game = Game(RandomPlayer, AlwaysCooperatePlayer, rounds, discount)
    history = game.run()
    curr_plays = history['RowAction'].tolist()

    diff = False
    for k in range(0,rounds):
        if prev_plays[k] != curr_plays[k]:
            diff = True
            break

    assert diff
