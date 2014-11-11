from dilemma.tournament import Tournament

from dilemma.player_ac import AlwaysCooperatePlayer
from dilemma.player_ad import AlwaysDefectPlayer


if __name__ == '__main__':
    agents = {
        'Always Cooperate': AlwaysCooperatePlayer,
        'Always Defect': AlwaysDefectPlayer
    }
    tournament = Tournament(agents)
    row, col = tournament.run()

    print ''
    print '-------------------'
    print 'Row Payoffs'
    print '-------------------'
    print row
    row.to_csv('row.csv')
    print '(saved to row.csv)'

    print ''
    print '-------------------'
    print 'Col Payoffs'
    print '-------------------'
    print col
    col.to_csv('col.csv')
    print '(saved to col.csv)'