from dilemma.player import Player


class CCDPlayer(Player):

    def get_action(self, history):
        """Player will play the following pattern: CCD

        See Player documentation for further details.
        """
        k = self.this_turn(history)
        if k % 3 == 2:
            return 'D'
        else:
            return 'C'
