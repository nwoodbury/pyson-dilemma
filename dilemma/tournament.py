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
