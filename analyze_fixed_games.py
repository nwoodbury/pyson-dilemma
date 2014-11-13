import pandas as pd

rounds = 10  # confusing, sorry, this is repetitions not rounds per game
lnths = [5, 100, 200]


if __name__ == '__main__':
    for l in lnths:
        lst = {}
        i = 0
        for rnd in range(rounds):
            fl = 'r_row_%i_%i.csv' % (rnd, l)
            lst[i] = pd.read_csv(fl, index_col=0)
            i += 1

        all_games = pd.Panel(lst).transpose(2, 0, 1)
        means = all_games.mean().applymap(lambda x: round(x, 1))
        stds = all_games.std().applymap(lambda x: round(x, 1))

        print 'Means (length = %i):' % l
        print means
        means.to_csv('f_means_%i.csv' % l)

        print ''
        print 'Standard Deviations (length = %i)' % l
        print stds
        stds.to_csv('f_stds_%i.csv' % l)

        # print all_games.max().applymap(lambda x: round(x, 1))
        # print all_games.min().applymap(lambda x: round(x, 1))
