from dilemma.player import Player

class NeverForgivePlayer(Player):

    def __init__(self, me):
        Player.__init__(self, me)
        self.cooperating = True


    def get_action(self, history):
        """Player will cooperate until the other player defects. Then the player will always defect.

        See Player documentation for further details.
        """
        if self.cooperating:
            if self.enemy_defected_last(history):
                self.cooperating = False
                return 'D'
            else:
                return 'C'
        else:
            return 'D'
