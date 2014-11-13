from dilemma.player import Player


class SwitchPlayer(Player):

    def __init__(self, me):
        Player.__init__(self, me)
        self.last = 'D'

    def get_action(self, history):
        """Always cooperates, independent of what the other player does.

        See Player documentation for further details.
        """
        if self.last == 'D':
            self.last = 'C'
            return 'C'
        else:
            self.last = 'D'
            return 'D'
