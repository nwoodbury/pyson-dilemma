from dilemma.player import Player


class AlwaysCooperatePlayer(Player):

    def get_action(self, history):
        """Always cooperates, independent of what the other player does.

        See Player documentation for further details.
        """
        return 'C'
