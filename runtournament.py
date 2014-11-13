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
    tournament = Tournament(agents)
    row, col = tournament.run()

    print('')
    print('-------------------')
    print('Row Payoffs')
    print('-------------------')
    print(row)
    row.to_csv('row.csv')
    print('(saved to row.csv)')

    print('')
    print('-------------------')
    print('Col Payoffs')
    print('-------------------')
    print(col)
    col.to_csv('col.csv')
    print('(saved to col.csv)')
