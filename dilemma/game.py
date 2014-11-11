import pandas as pd

# Outer dict is row action, inner is col action.
# Payoffs in form (row, col)
PAYOFFS = {
    'C': {'C': (3, 3), 'D': (0, 5)},
    'D': {'C': (5, 0), 'D': (1, 1)}
}


class Game:
    """Runs a repeated play game competing two agents.

    The payoff to each player i at time k will be:

        v_i(k) = r^k * u_i(a_r(k), a_c(k)),

    where r is `discount` and u_i(a_r(k), a_c(k)) is the utility to i at time k
    given the pair of actions played by each player at k. This is given by
    `self.payoffs[a_r(k)][a_c(k)][i], where i = 0 for the row player, 1 for the
    column player, and a_r(k), a_c(k) in {'C', 'D'}.

    And the tot

    Parameters
    ----------
    row_player : Player
        The row player in the game.
    col_player : Player
        The column player in the game.
    rounds : int
        The number of rounds for which the game will last. For the tournament,
        this should be some large random number. For testing, this can be
        smaller and deterministic.
    discount : number [0, 1]
        The discount factor r.
    payoffs : dictionary of dictionaries
        The payoff matrix for the game. The outer dictionary is a mapping of
        actions by the row player to dictionaries. The nested dictionaries
        is a mapping of actions by the column player to a tuple of payoffs,
        where the first entry is the payoff to the row player and the second
        entry is the payoff to the column player.

        If not given, this defaults to the PAYOFFS dictionary defined at the
        top of this file. Refer to this object for an example of how to create
        a payoff matrix. This default likely will not need to be changed.
    """

    def __init__(self, row_player, col_player, rounds, discount,
                 payoffs=PAYOFFS):
        self.row_player = row_player
        self.col_player = col_player
        self.rounds = rounds
        self.discount = discount
        self.payoffs = payoffs

        self.history = {}

    def run(self):
        for k in range(self.rounds):
            if k > 0:
                df_history = pd.DataFrame(self.history)
            else:
                df_history = None
            print df_history
            row_a = self.row_player.get_action(df_history)
            col_a = self.col_player.get_action(df_history)
            assert row_a in ['C', 'D']
            assert col_a in ['C', 'D']
            uk = self.uk(row_a, col_a, k)
            self.history[k] = {
                'RowAction': row_a,
                'ColAction': col_a,
                'RowPayoff': uk[0],
                'ColPayoff': uk[1]
            }
        return pd.DataFrame(self.history)

    def u(self, row_action, col_action):
        """Gets the payoffs to both players given the actions by each player.

        Parameters
        ----------
        row_action : str in {'C', 'D'}
            The action performed by the row player.
        col_action : str in {'C', 'D'}
            The action performed by the column player.

        Returns
        -------
        payoffs : tuple (size 2) of numbers
            The first entry in the tuple is the payoff to the row player, and
            the second entry is the payoff to the column player.
        """
        return self.payoffs[row_action][col_action]

    def uk(self, row_action, col_action, k, round_to=6):
        """Gets the payoffs to both players at time k, given the actions by
        each player.

        Parameters
        ----------
        row_action : str in {'C', 'D'}
            The action performed by the row player.
        col_action : str in {'C', 'D'}
            The action performed by the column player.
        k : int (non-negative)
            The time at which to discount the payoffs. The first time is 0.
        round_to : int
            The number of decimal places at which to round the solution.
            Defaults to 6.

        Returns
        -------
        payoffs : tuple (size 2) of numbers
            The first entry in the tuple is the payoff to the row player, and
            the second entry is the payoff to the column player. These payoffs
            are discounted.
        """
        u = self.u(row_action, col_action)
        return (round(u[0] * self.discount ** k, round_to),
                round(u[1] * self.discount ** k, round_to))
