This script uses a Constraint Satisfaction Problem solving framework to solve the real-life problem I have faced, of assigning eSports competitors to valid round-robin pools while considering "conflicts" they should not play against.

The framework code in ``csp.py`` is mainly lifted from David Kopec's ``Classic Computer Science Problems in Python``, and extended with a few custom constraints. By specifying a list of competitor usernames and an arbitrary sequence of constraints in ``pools.py``,  the script will generate all valid combinations of players in round-robin pools, where they avoid (or are forced to play) certain players as is considered appropriate.

**CONSIDERATIONS**

While this tool has proved useful (from the perspective of a tournament organizer) for the sake of visualizing interesting pools, it does not contain any metric of reference for actual seeding (the practice of distributing players of similar skill levels evenly throughout pools, so no pool is under- or over-powered). This is a definite goal I wish to achieve in the future.

Since this script is not currently capable of such seeding, if you are one of the real-world players who recognizes their tag in this script - hello! And don't worry, there's a good chance the constraints here didn't end up being applied during the actual seeding of a certain tournament it was used for...
