from dilemma.player import Player


class AlwaysDefectPlayer(Player):

    def get_action(self, history):
        """Always defects, independent of what the other player does.

        See Player documentation for further details.
        """
        return 'D'
