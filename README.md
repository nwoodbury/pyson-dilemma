pyson-dilemma
=============

BYU CS 670 Repeated Play Prisoner's Dilemma Lab.

Installation
------------

Install with:

    python setup.py develop --user


Testing
-------

Test cases should be run before committing any changes. To run the test cases:

    python setup.py test

Running a Tournament
--------------------

Run the tournament with:

    python runtournament.py

The tournament results will be saved in `row.csv` (payoffs to the row player)
when matched with the column player and `col.csv` (payoffs to the column
player when the row player is matched to the column player). If all agents
are deterministic, then `row.csv` will be the transpose of `col.csv`; otherwise
they should be close to being transposes.

Also, the history of each pairing will be stored in directory `histories/`,
where each file is named `ROWPLAYER_vs_COLPLAYER.csv`.

Creating an Agent
-----------------

Follow these steps to create an agent and register it in the tournament:

1. Create the file in which the agent class will reside in the `dilemma/`
   directory. By convention, the file is named `player_abbr.py`,
   where abbr is an abbreviation (lower case) of the player's name. For
   example, `player_ac.py` for Always Cooperate.
1. In `player_abbr.py`, create a class for the player that inherits the
   `Player` class found in `player.py`. By convention, the player's class is
   in camelcase and named `PlayerNamePlayer` where `PlayerName` is any name.
   For example, `AlwaysCooperatePlayer` for Always Cooperate.
1. Override the `get_action()` method in the `PlayerNamePlayer` class, defining
   how the player makes choices based on the past history. Refer to the helper
   functions in class `Player` in `player.py` for useful utilities to interact
   with the `history` object.
1. In `runtournament.py`, import the player class:

        from dilemma.player_abbr import PlayerNamePlayer

1. In `runtournament.py`, add an entry in the `agents` dictionary mapping
   the player's name to the player's class:

        agents = {
            ...,
            'Player Name': PlayerNamePlayer
        }

1. The player is ready to go, run the tournament as described above.
1. Don't forget to add the `player_abbr.py` file to the repo:

        git add dilemma/player_abbr.py

   and then commit and push the changes:

        git commit -a
        git push
