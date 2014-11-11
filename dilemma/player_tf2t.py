from dilemma.player import Player

class TitFor2TatsPlayer(Player):

    def get_action(self, history):
        """Player will defect after the other player defects twice and will cooperate after the other player
           cooperates once

        See Player documentation for further details.
        """
        k_last = self.last_turn()
        last_action = self.my_actions(history)[k_last]
        if self.count_defects(history, 1) == 0:
            return 'C'
        if self.count_defects(history, 2) == 2:
            return 'D'
        return last_action