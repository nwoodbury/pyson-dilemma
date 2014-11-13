from dilemma.player import Player


AC_RESP = ['C', 'C', 'C', 'C']
AD_RESP = ['D', 'D', 'D', 'D']
CCD_RESP = ['C', 'C', 'D', 'C']
NF_RESP = ['C', 'D', 'D', 'D']
OMNI_RESP = ['D', 'D', 'C', 'C']
PAVLOV_RESP = ['C', 'D', 'C', 'C']
TF2T_RESP = ['C', 'C', 'D', 'C']
TFT_RESP = ['C', 'D', 'D', 'C']

class OmniPlayer(Player):

    def __init__(self, me):
            Player.__init__(self, me)
            self.first_four_moves = ['D', 'D', 'C', 'C']
            self.enemy_strat = 'rnd'

    def get_action(self, history):
        """Player will attempt to find out enemy's strategy and then create a strategy that gets the best results

        See Player documentation for further details.
        """
        k = self.this_turn(history)
        if k < 4:
            return self.first_four_moves[k]
        if k == 4:
            enemy_actions = self.enemy_actions(history)
            if enemy_actions == AC_RESP:
                self.enemy_strat = 'ac'
            elif enemy_actions == AD_RESP:
                self.enemy_strat = 'ad'
            elif enemy_actions == CCD_RESP:
                self.enemy_strat = 'ccd'
            elif enemy_actions == NF_RESP:
                self.enemy_strat = 'nf'
            elif enemy_actions == OMNI_RESP:
                self.enemy_strat = 'omni'
            elif enemy_actions == PAVLOV_RESP:
                self.enemy_strat = 'pavlov'
            elif enemy_actions == TF2T_RESP:
                self.enemy_strat = 'tf2t'
            elif enemy_actions == TFT_RESP:
                self.enemy_strat = 'tft'

        if self.enemy_strat == 'omni' or self.enemy_strat == 'tft':
            return 'C'
        elif self.enemy_strat == 'pavlov':
            if k == 4:
                return 'D'
            else:
                return 'C'
        elif self.enemy_strat == 'tf2t':
            if k % 2 == 0:
                return 'D'
            else:
                return 'C'
        else:
            return 'D'
