from dilemma.player import Player

class WinStayLoseShiftPlayer(Player):

    def __init__(self, me, game):
        Player.__init__(self, me)
        self.thresh = game.payoffs['C']['C']

    def get_action(self, history):
        """Player will change play only if he did not receive the highest or 2nd-highest reward last turn

        See Player documentation for further details.
        """
        k_last = self.last_turn(history)
        last_payoff = self.my_payoffs(history)[k_last]
        last_play = self.my_actions(history)[k_last]
        if last_payoff >= self.thresh:
            return last_play
        if last_play == 'C':
            return 'D'
        else:
            return 'C'