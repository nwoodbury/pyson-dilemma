

class Player:
    """Base class for all players that play in the tournament.

    Parameters
    ----------
    me : str in {'Row', 'Column'} (case sensitive)
        Whether this player is the row or the column player.

    Class Variables
    ---------------
    me : str in {'Row', 'Column'} (case sensitive)
        Whether this player is the row or the column player.
    enemy : str in {'Row', 'Column'} (case sensitive)
        Whether the other player is the row or the column player.

    Methods to Override
    -------------------
    * get_action
    """

    def __init__(self, me):
        """Constructor.

        Note: If the constructor is overriden, the child constructor must call:

            Player.__init__(self, me),

        presumably at the first line of the constructor, though potentially
        in another line.
        """
        assert me in ['Row', 'Col']
        self.me = me
        if self.me == 'Row':
            self.enemy = 'Col'
        else:
            self.enemy = 'Row'

    def get_action(self, history):
        """MUST BE OVERRIDDEN BY THE SUBCLASS.

        Gets the action of the player at the next time (defined as the time
        after the most recent time in history).

        Parameters
        ----------
        history : pandas.DataFrame or None
            The dataframe that contains the history of the game up to the
            present. Rows are sorted in order of time, and indexed by k. The
            columns, for each row indexed by time k, are as follows:

                * `RowAction`: The action performed by the row player at
                  time k.

                * `ColAction`: The action performed by the column player at
                  time k.

                * `RowPayoff`: The discounted payoff to the row player at
                  time k.

                * `ColPayoff`: The discounted payoff to the column player at
                  time k.

            If None is given instead of the history, then this is the first
            turn (None will always be given on the first turn).

            The utility functions defined at the end of this class will
            be helpful for extracting useful information from the history
            object. See the documentation of those functions for more info.

        Returns
        -------
        action : str in {'C', 'D'}
            The action performed by this player at this time.
        """
        raise NotImplemented()

    ###########################################################################
    # Utility Functions
    ###########################################################################

    def last_turn(self, history):
        """Returns the index (k) of the last turn, as seen by `history`.
        If this is the first turn, returns -1.

        Parameters
        ----------
        history : pandas.DataFrame
            See documentation for `get_action`.

        Returns
        -------
        k : int
            The index of the last turn in `history`.
        """
        if history is None:
            return -1
        return history.axes[0][-1]

    def this_turn(self, history):
        """Returns the index (k) of the current turn.

        Parameters
        ----------
        history : pandas.DataFrame
            See documentation for `get_action`.

        Returns
        -------
        k : int
            The index of the current turn.
        """
        return self.last_turn(history) + 1

    def my_actions(self, history):
        """Returns a list of my actions, where actions[k] is my action at
        time k.

        Parameters
        ----------
        history : pandas.DataFrame
            See documentation for `get_action`.

        Returns
        -------
        actions : list
            The list of this player's actions, where actions[k] is the action
            performed at time k.
        """
        if history is None:
            return []
        return history['%sAction' % self.me].tolist()

    def enemy_actions(self, history):
        """Returns a list of the enemy's actions, where actions[k] is the
        enemy's action at time k.

        Parameters
        ----------
        history : pandas.DataFrame
            See documentation for `get_action`.

        Returns
        -------
        actions : list
            The list of the other player's actions, where actions[k] is the
            action performed at time k.
        """
        if history is None:
            return []
        return history['%sAction' % self.enemy].tolist()

    def my_payoffs(self, history):
        """Returns a list of my payoffs, where payoffs[k] is my discounted
        payoff at time k.

        Parameters
        ----------
        history : pandas.DataFrame
            See documentation for `get_action`.

        Returns
        -------
        payoffs : list
            The list of this player's payoffs, where payoffs[k] is the
            discounted payoff at time k.
        """
        if history is None:
            return []
        return history['%sPayoff' % self.me].tolist()

    def enemy_payoffs(self, history):
        """Returns a list of my enemy's payoffs, where payoffs[k] is the
        enemy's discounted payoff at time k.

        Parameters
        ----------
        history : pandas.DataFrame
            See documentation for `get_action`.

        Returns
        -------
        payoffs : list
            The list of the other player's payoffs, where payoffs[k] is the
            discounted payoff at time k.
        """
        if history is None:
            return []
        return history['%sPayoff' % self.enemy].tolist()

    def count_defects(self, history, n):
        """Returns the number of times the enemy has defected in the last n
        turns.

        Parameters
        ----------
        history : pandas.DataFrame
            See documentation for `get_action`.
        n : int (positive)
            The number of turns in the past to look for defects. If n is less
            than the number of rounds seen in the game m, then will only look
            at the last m rounds.

        Returns
        -------
        defects : int (non-negative)
            The count of times the enemy has defected in the last n turns.
        """
        if history is None:
            return 0
        df = history.tail(n)
        df = df[df['%sAction' % self.enemy] == 'D']
        return len(df)

    def enemy_defected_last(self, history):
        """Returns whether the enemy defected last turn.

        Parameters
        ----------
        history : pandas.DataFrame
            See documentation for `get_action`.

        Returns
        -------
        defected : boolean
            True if the enemy defected last turn, false otherwise.
        """
        return self.count_defects(history, 1) == 1
