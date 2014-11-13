from dilemma.player import Player


class PavlovPlayer(Player):

    def get_action(self, history):
        """Player will defect if the 2 players did not agree on the previous turn, otherwise it will cooperate

        See Player documentation for further details.
        """
        k_last = self.last_turn(history)
        if k_last == -1:
            return 'C'
        my_last_action = self.my_actions(history)[k_last]
        enemy_last_action = 'C'
        if self.enemy_defected_last(history):
            enemy_last_action = 'D'
        if my_last_action == enemy_last_action:
            return 'C'
        else:
            return 'D'