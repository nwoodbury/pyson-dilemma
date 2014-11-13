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


discounts = [0.75, 0.9, 0.99]
trials = 10


def run_instance(agents, trial_no, discount):
    print('')
    print('====================================================')
    print('Trial #%i, p=%.2f' % (trial_no, discount))
    print('====================================================')

    tournament = Tournament(agents)
    row, col = tournament.run(p=discount)

    print('')
    print('-------------------')
    print('Row Payoffs')
    print('-------------------')
    print(row)
    row_name = 'row_%i_%i.csv' % (trial_no, int(discount * 100))
    row.to_csv(row_name)
    print('(saved to %s)' % row_name)

    print('')
    print('-------------------')
    print('Col Payoffs')
    print('-------------------')
    print(col)
    col_name = 'col_%i_%i.csv' % (trial_no, int(discount * 100))
    col.to_csv(col_name)
    print('(saved to %s)' % col_name)


def run_trial(agents):
    for trial in range(trials):
        for discount in discounts:
            run_instance(agents, trial, discount)


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
