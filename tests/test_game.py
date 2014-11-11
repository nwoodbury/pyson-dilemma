from dilemma.game import Game
from dilemma.player_ac import AlwaysCooperatePlayer


class TestGameStatic(object):

    def setup(self):
        # This is the same as defined in Axelrod, and likely the same that is
        # the default to Game. Redefined here to guarantee correctness in
        # testing.
        payoffs = {
            'C': {'C': (3, 3), 'D': (0, 5)},
            'D': {'C': (5, 0), 'D': (1, 1)}
        }
        self.game = Game(AlwaysCooperatePlayer, AlwaysCooperatePlayer, 10, 0.9,
                         payoffs)

    def test_payoffs_cc(self):
        assert self.game.u('C', 'C') == (3, 3)

    def test_payoffs_cd(self):
        assert self.game.u('C', 'D') == (0, 5)

    def test_payoffs_dc(self):
        assert self.game.u('D', 'C') == (5, 0)

    def test_payoffs_dd(self):
        assert self.game.u('D', 'D') == (1, 1)

    def test_discount_cd_0(self):
        assert self.game.uk('C', 'D', 0) == (0, 5)

    def test_discount_dc_1(self):
        assert self.game.uk('D', 'C', 1) == (4.5, 0)

    def test_discount_cc_2(self):
        assert self.game.uk('C', 'C', 2) == (2.43, 2.43)

    def test_discount_dd_3(self):
        assert self.game.uk('D', 'D', 3) == (0.729, 0.729)
