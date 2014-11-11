from dilemma.tournament import Game


class TestGameStatic(object):

    def setup(self):
        # This is the same as defined in Axelrod, and likely the same that is
        # the default to Game. Redefined here to guarantee correctness in
        # testing.
        payoffs = {
            'C': {'C': (3, 3), 'D': (0, 5)},
            'D': {'C': (5, 0), 'D': (1, 1)}
        }
        self.game = Game(None, None, 10, 0.9, payoffs)

    def test_payoffs_cc(self):
        assert self.game.u('C', 'C') == (3, 3)

    def test_payoffs_cd(self):
        assert self.game.u('C', 'D') == (0, 5)

    def test_payoffs_dc(self):
        assert self.game.u('D', 'C') == (5, 0)

    def test_payoffs_dd(self):
        assert self.game.u('D', 'D') == (1, 1)