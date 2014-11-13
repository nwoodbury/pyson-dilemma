import random
from dilemma.player import Player


class TitForRandomTatsPlayer(Player):

    def __init__(self, me):
        Player.__init__(self, me)
        self.probs = [0.1, 0.5, 0.75, 0.9, 1]
        self.zero_last = False
        self.zero_before_last = False

    def get_action(self, history):
        """Tit for tat with a random action.

        See Player documentation for further details.
        """

        defected_last = self.enemy_defected_last(history)

        action = 'C'
        self.zero_last = False

        # Check to see if the zero probability was triggered in the turn
        # before last turn, if so, update the zero probability according to
        # how the enemy responded.
        should_punish = True
        if self.zero_before_last:
            if defected_last:
                # Enemy punished, cut zero probability in half
                self.probs[0] /= 2.0
                should_punish = False
            else:
                # Enemy ignored defect, increment probability by 10%
                self.probs[0] = min(self.probs[0] + 0.1, 1.0)

        if should_punish:

            # If the player cooperated last, check to see if we should test
            # them
            if not defected_last:
                if self._should_defect(self.probs[0]):
                    self.zero_last = True
                    action = 'D'

            # Check to see if the player has defected n times in the last n
            # turns, if so, defect with probability given by self.probs
            for n in range(1, 5):
                if self.count_defects(history, n=n) == n and \
                        self._should_defect(self.probs[n]):
                    action = 'D'

        self.zero_before_last = self.zero_last
        return action

    def _should_defect(self, probability, exploited_last=False):
        """Returns True with probability `probability`.
        """
        rdm = random.random()
        return rdm <= probability
