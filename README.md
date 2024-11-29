This script uses a Constraint Satisfaction Problem solving framework to solve the real-life problem I have faced, of assigning eSports competitors to valid round-robin pools while considering "conflicts" they should not play against.

The framework code in ``csp.py`` is mainly lifted from David Kopec's ``Classic Computer Science Problems in Python``, and extended with a few custom constraints. By specifying a list of competitor usernames and an arbitrary sequence of constraints in ``pools.py``,  the script will generate all valid combinations of players in round-robin pools, where they avoid (or are forced to play) certain players as is considered appropriate.
