import os
import random
import pandas as pd

from dilemma.game import Game


class Tournament:
    """Runs a tournament pitting all players against all other players
    (including itself).

    Parameters
    ----------
    agents : dictionary of classes
        A dictionary mapping agent name to the class (not object) that
        creates that agent.
    """

    def __init__(self, agents):
        self.row = {}
        self.col = {}
        self.agents = agents

    def run(self, progress=True):
        """Runs the tournament.

        Parameters
        ----------
        progress : boolean
            True if progress messages should be printed to the command line,
            false otherwise.

        Returns
        -------
        row_results : pandas.DataFrame
            The rows name row players, and the columns name column players.
            Each entry is the score of the row playing against the column
            player. Also contains a `Totals` row and column.
        col_results : pandas.DataFrame
            The rows name row players and the columns name column players.
            Each entry is the score of the column playing against the row
            player. For deterministic agents, this will be the transpose of
            `row_results`, for stochastic players, it should be close but not
            the same as the transpose. Also contains a `Totals` row and column.
        """

        # see documentation of the game constructor for motivation of this
        # choice of rounds.
        rounds = random.randint(160, 320)
        #rounds = 5
        discount = 0.9

        total = len(self.agents) ** 2
        count = 0

        if not os.path.exists('histories/'):
            os.makedirs('histories/')

        if progress:
            print('-------------------')
            print('Running Tournament:')
        for row_name, row_class in self.agents.items():
            self.row[row_name] = {}
            self.col[row_name] = {}
            for col_name, col_class in self.agents.items():
                game = Game(row_class, col_class, rounds, discount)
                history = game.run()
                row_payoffs = history['RowPayoff'].sum()
                col_payoffs = history['ColPayoff'].sum()
                self.row[row_name][col_name] = row_payoffs
                self.col[row_name][col_name] = col_payoffs

                history.to_csv('histories/%s_vs_%s.csv' % (row_name, col_name))

                count += 1
                if progress:
                    print('\t%.2f%% Complete' % (count * 100 / float(total)))

        if progress:
            print('\tDone.')
            print('-------------------')

        row = pd.DataFrame(self.row).transpose()
        col = pd.DataFrame(self.col).transpose()

        row = self._add_totals(row)
        col = self._add_totals(col)

        return row, col

    def _add_totals(self, df):
        """Adds totals row and column to the dataframe.

        Parameters
        ----------
        df : pandas.DataFrame
            The dataframe to add totals to.

        Returns
        -------
        df : pandas.DataFrame
            The dataframe with totals added.
        """
        df['Totals'] = df.sum(axis=1)
        df = df.transpose()
        df['Totals'] = df.sum(axis=1)
        df = df.transpose()
        #df['Totals']['Totals'] = None  # Don't total the totals
        return df
