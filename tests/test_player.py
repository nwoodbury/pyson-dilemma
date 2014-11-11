import pandas as pd
from dilemma.player import Player


class TestPlayer(object):

    def _to_history(self, arr):
        hist = {}
        for k in range(len(arr)):
            hist[k] = {
                'RowAction': arr[k][0],
                'ColAction': arr[k][1],
                'RowPayoff': arr[k][2],
                'ColPayoff': arr[k][3]
            }
        return pd.DataFrame(hist).transpose()

    def setup(self):
        self.history_0 = None
        self.history_1 = self._to_history(
            [
                ['C', 'C', 3, 3]
            ]
        )
        self.history_2 = self._to_history(
            [
                ['C', 'C', 3, 3],
                ['C', 'D', 0, 5 * .9]
            ]
        )
        self.history_3 = self._to_history(
            [
                ['C', 'C', 3, 3],
                ['C', 'D', 0, 5 * .9],
                ['C', 'D', 0, 5 * .9 ** 2]
            ]
        )
        self.history_4 = self._to_history(
            [
                ['C', 'C', 3, 3],
                ['C', 'D', 0, 5 * .9],
                ['C', 'D', 0, 5 * .9 ** 2],
                ['D', 'C', 5 * .9 ** 3, 0]
            ]
        )
        self.row = Player('Row')
        self.col = Player('Col')

    ###########################################################################
    #   Round 0
    ###########################################################################

    def test_last_turn_0(self):
        assert self.row.last_turn(self.history_0) == -1
        assert self.col.last_turn(self.history_0) == -1

    def test_this_turn_0(self):
        assert self.row.this_turn(self.history_0) == 0
        assert self.col.this_turn(self.history_0) == 0

    def test_my_actions_turn_0(self):
        assert self.row.my_actions(self.history_0) == []
        assert self.col.my_actions(self.history_0) == []

    def test_enemy_actions_turn_0(self):
        assert self.row.enemy_actions(self.history_0) == []
        assert self.col.enemy_actions(self.history_0) == []

    def test_my_payoffs_turn_0(self):
        assert self.row.my_payoffs(self.history_0) == []
        assert self.col.my_payoffs(self.history_0) == []

    def test_enemy_payoffs_turn_0(self):
        assert self.row.enemy_payoffs(self.history_0) == []
        assert self.col.enemy_payoffs(self.history_0) == []

    def test_count_defects_turn_0(self):
        assert self.row.count_defects(self.history_0, 1) == 0
        assert self.row.count_defects(self.history_0, 2) == 0

        assert self.col.count_defects(self.history_0, 1) == 0
        assert self.col.count_defects(self.history_0, 2) == 0

    def test_enemy_defected_last_turn_0(self):
        assert self.row.enemy_defected_last(self.history_0) is False
        assert self.col.enemy_defected_last(self.history_0) is False

    ###########################################################################
    #   Round 1
    ###########################################################################

    def test_last_turn_1(self):
        assert self.row.last_turn(self.history_1) == 0
        assert self.col.last_turn(self.history_1) == 0

    def test_this_turn_1(self):
        assert self.row.this_turn(self.history_1) == 1
        assert self.col.this_turn(self.history_1) == 1

    def test_my_actions_turn_1(self):
        assert self.row.my_actions(self.history_1) == ['C']
        assert self.col.my_actions(self.history_1) == ['C']

    def test_enemy_actions_turn_1(self):
        assert self.row.enemy_actions(self.history_1) == ['C']
        assert self.col.enemy_actions(self.history_1) == ['C']

    def test_my_payoffs_turn_1(self):
        assert self.row.my_payoffs(self.history_1) == [3]
        assert self.col.my_payoffs(self.history_1) == [3]

    def test_enemy_payoffs_turn_1(self):
        assert self.row.enemy_payoffs(self.history_1) == [3]
        assert self.col.enemy_payoffs(self.history_1) == [3]

    def test_count_defects_turn_1(self):
        assert self.row.count_defects(self.history_1, 1) == 0
        assert self.row.count_defects(self.history_1, 2) == 0

        assert self.col.count_defects(self.history_1, 1) == 0
        assert self.col.count_defects(self.history_1, 2) == 0

    def test_enemy_defected_last_turn_1(self):
        assert self.row.enemy_defected_last(self.history_1) is False
        assert self.col.enemy_defected_last(self.history_1) is False

    ###########################################################################
    #   Round 2
    ###########################################################################

    def test_last_turn_2(self):
        assert self.row.last_turn(self.history_2) == 1
        assert self.col.last_turn(self.history_2) == 1

    def test_this_turn_2(self):
        assert self.row.this_turn(self.history_2) == 2
        assert self.col.this_turn(self.history_2) == 2

    def test_my_actions_turn_2(self):
        assert self.row.my_actions(self.history_2) == ['C', 'C']
        assert self.col.my_actions(self.history_2) == ['C', 'D']

    def test_enemy_actions_turn_2(self):
        assert self.row.enemy_actions(self.history_2) == ['C', 'D']
        assert self.col.enemy_actions(self.history_2) == ['C', 'C']

    def test_my_payoffs_turn_2(self):
        assert self.row.my_payoffs(self.history_2) == [3, 0]
        assert self.col.my_payoffs(self.history_2) == [3, 5 * .9]

    def test_enemy_payoffs_turn_2(self):
        assert self.row.enemy_payoffs(self.history_2) == [3, 5 * .9]
        assert self.col.enemy_payoffs(self.history_2) == [3, 0]

    def test_count_defects_turn_2(self):
        assert self.row.count_defects(self.history_2, 1) == 1
        assert self.row.count_defects(self.history_2, 2) == 1
        assert self.row.count_defects(self.history_2, 3) == 1

        assert self.col.count_defects(self.history_2, 1) == 0
        assert self.col.count_defects(self.history_2, 2) == 0
        assert self.col.count_defects(self.history_2, 3) == 0

    def test_enemy_defected_last_turn_2(self):
        assert self.row.enemy_defected_last(self.history_2) is True
        assert self.col.enemy_defected_last(self.history_2) is False

    ###########################################################################
    #   Round 3
    ###########################################################################

    def test_last_turn_3(self):
        assert self.row.last_turn(self.history_3) == 2
        assert self.col.last_turn(self.history_3) == 2

    def test_this_turn_3(self):
        assert self.row.this_turn(self.history_3) == 3
        assert self.col.this_turn(self.history_3) == 3

    def test_my_actions_turn_3(self):
        assert self.row.my_actions(self.history_3) == ['C', 'C', 'C']
        assert self.col.my_actions(self.history_3) == ['C', 'D', 'D']

    def test_enemy_actions_turn_3(self):
        assert self.row.enemy_actions(self.history_3) == ['C', 'D', 'D']
        assert self.col.enemy_actions(self.history_3) == ['C', 'C', 'C']

    def test_my_payoffs_turn_3(self):
        assert self.row.my_payoffs(self.history_3) == [3, 0, 0]
        assert self.col.my_payoffs(self.history_3) == [3, 5 * .9, 5 * .9 ** 2]

    def test_enemy_payoffs_turn_3(self):
        assert self.row.enemy_payoffs(self.history_3) == \
            [3, 5 * .9, 5 * .9 ** 2]
        assert self.col.enemy_payoffs(self.history_3) == [3, 0, 0]

    def test_count_defects_turn_3(self):
        assert self.row.count_defects(self.history_3, 1) == 1
        assert self.row.count_defects(self.history_3, 2) == 2
        assert self.row.count_defects(self.history_3, 3) == 2
        assert self.row.count_defects(self.history_3, 4) == 2

        assert self.col.count_defects(self.history_3, 1) == 0
        assert self.col.count_defects(self.history_3, 2) == 0
        assert self.col.count_defects(self.history_3, 3) == 0
        assert self.col.count_defects(self.history_3, 4) == 0

    def test_enemy_defected_last_turn_3(self):
        assert self.row.enemy_defected_last(self.history_3) is True
        assert self.col.enemy_defected_last(self.history_3) is False

    ###########################################################################
    #   Round 4
    ###########################################################################

    def test_last_turn_4(self):
        assert self.row.last_turn(self.history_4) == 3
        assert self.col.last_turn(self.history_4) == 3

    def test_this_turn_4(self):
        assert self.row.this_turn(self.history_4) == 4
        assert self.col.this_turn(self.history_4) == 4

    def test_my_actions_turn_4(self):
        assert self.row.my_actions(self.history_4) == ['C', 'C', 'C', 'D']
        assert self.col.my_actions(self.history_4) == ['C', 'D', 'D', 'C']

    def test_enemy_actions_turn_4(self):
        assert self.row.enemy_actions(self.history_4) == ['C', 'D', 'D', 'C']
        assert self.col.enemy_actions(self.history_4) == ['C', 'C', 'C', 'D']

    def test_my_payoffs_turn_4(self):
        assert self.row.my_payoffs(self.history_4) == [3, 0, 0, 5 * .9 ** 3]
        assert self.col.my_payoffs(self.history_4) == \
            [3, 5 * .9, 5 * .9 ** 2, 0]

    def test_enemy_payoffs_turn_4(self):
        assert self.row.enemy_payoffs(self.history_4) == \
            [3, 5 * .9, 5 * .9 ** 2, 0]
        assert self.col.enemy_payoffs(self.history_4) == \
            [3, 0, 0, 5 * .9 ** 3]

    def test_count_defects_turn_4(self):
        assert self.row.count_defects(self.history_4, 1) == 0
        assert self.row.count_defects(self.history_4, 2) == 1
        assert self.row.count_defects(self.history_4, 3) == 2
        assert self.row.count_defects(self.history_4, 4) == 2
        assert self.row.count_defects(self.history_4, 5) == 2

        assert self.col.count_defects(self.history_4, 1) == 1
        assert self.col.count_defects(self.history_4, 2) == 1
        assert self.col.count_defects(self.history_4, 3) == 1
        assert self.col.count_defects(self.history_4, 4) == 1
        assert self.col.count_defects(self.history_4, 5) == 1

    def test_enemy_defected_last_turn_4(self):
        assert self.row.enemy_defected_last(self.history_4) is False
        assert self.col.enemy_defected_last(self.history_4) is True
