from dilemma.player import Player


class WinStayLoseShiftPlayer(Player):

    def get_action(self, history):
        """Player will change play only if he did not receive the highest or 2nd-highest reward last turn

        See Player documentation for further details.
        """
        k_last = self.last_turn(history)
        if k_last == -1:
            return 'C'
        my_last_play = self.my_actions(history)[k_last]
        if not self.enemy_defected_last(history):
            return my_last_play
        if my_last_play == 'C':
            return 'D'
        else:
            return 'C'