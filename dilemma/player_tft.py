from dilemma.player import Player


class TitForTatPlayer(Player):

    def get_action(self, history):
        """Always defects, independent of what the other player does.

        See Player documentation for further details.
        """
        if self.enemy_defected_last(history):
            return 'D'
        else:
            return 'C'
