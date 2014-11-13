from dilemma.tournament import Tournament

from dilemma.player_ac import AlwaysCooperatePlayer
from dilemma.player_ad import AlwaysDefectPlayer
from dilemma.player_tft import TitForTatPlayer
from dilemma.player_nf import NeverForgivePlayer
from dilemma.player_pavlov import PavlovPlayer
from dilemma.player_rnd import RandomPlayer
from dilemma.player_tf2t import TitFor2TatsPlayer
from dilemma.player_wsls import WinStayLoseShiftPlayer
from dilemma.player_ccd import CCDPlayer
from dilemma.player_omni import OmniPlayer
from dilemma.player_tfrt import TitForRandomTatsPlayer
from dilemma.player_switch import SwitchPlayer


rnds = [5, 100, 200]
trials = 10


def run_instance(agents, trial_no, rnd):
    print('')
    print('====================================================')
    print('Trial #%i, rounds=%.2f' % (trial_no, rnd))
    print('====================================================')

    tournament = Tournament(agents)
    row, col = tournament.run(rounds=rnd)

    print('')
    print('-------------------')
    print('Row Payoffs')
    print('-------------------')
    print(row)
    row_name = 'r_row_%i_%i.csv' % (trial_no, rnd)
    row.to_csv(row_name)
    print('(saved to %s)' % row_name)

    print('')
    print('-------------------')
    print('Col Payoffs')
    print('-------------------')
    print(col)
    col_name = 'r_col_%i_%i.csv' % (trial_no, rnd)
    col.to_csv(col_name)
    print('(saved to %s)' % col_name)


def run_trial(agents):
    for trial in range(trials):
        for rnd in rnds:
            run_instance(agents, trial, rnd)


if __name__ == '__main__':
    agents = {
        'Always Cooperate': AlwaysCooperatePlayer,
        'Always Defect': AlwaysDefectPlayer,
        'Tit-for-Tat': TitForTatPlayer,
        'Never Forgive': NeverForgivePlayer,
        'Pavlov': PavlovPlayer,
        'Random': RandomPlayer,
        'Tit-for-2-Tats': TitFor2TatsPlayer,
        'Win-Stay-Lose-Shift': WinStayLoseShiftPlayer,
        'CCD': CCDPlayer,
        'Omni': OmniPlayer,
        'Tit-for-Random-Tats': TitForRandomTatsPlayer,
        'Switch': SwitchPlayer
    }
    run_trial(agents)
