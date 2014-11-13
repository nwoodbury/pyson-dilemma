import pandas as pd

rounds = 10
discounts = [0.75, 0.9, 0.99]


if __name__ == '__main__':
    for p in discounts:
        lst = {}
        i = 0
        p100 = int(p * 100)
        for rnd in range(rounds):
            fl = 'row_%i_%i.csv' % (rnd, p100)
            lst[i] = pd.read_csv(fl, index_col=0)
            i += 1

        all_games = pd.Panel(lst).transpose(1, 0, 2)
        means = all_games.mean().applymap(lambda x: round(x, 1))
        stds = all_games.std().applymap(lambda x: round(x, 1))

        print 'Means (p = %.2f):' % p
        print means
        means.to_csv('means_%i.csv' % p100)

        print ''
        print 'Standard Deviations (p = %.2f)' % p
        print stds
        stds.to_csv('stds_%i.csv' % p100)

        # print all_games.max().applymap(lambda x: round(x, 1))
        # print all_games.min().applymap(lambda x: round(x, 1))
