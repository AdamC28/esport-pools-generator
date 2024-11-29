from csp import Constraint, CSP
from typing import Dict, List, Optional

class PoolExclusionConstraint(Constraint[str, str]):
    def __init__(self, p1: str, p2: str) -> None:
        super().__init__([p1, p2])
        self.p1: str = p1
        self.p2: str = p2

    def satisfied(self, assignment: Dict[str, str]) -> bool:
        # If either player is not in the assignment, then it is not
        # yet possible for their pools to be conflicting
        if self.p1 not in assignment or self.p2 not in assignment:
            return True
        
        # check the pool assigned to place1 is not the same as the
        # pool assigned to place2
        return assignment[self.p1] != assignment[self.p2]

class PoolSizeConstraint(Constraint[str, int]):
    def __init__(self, players: List[str], size: int) -> None:
        super().__init__(players)
        self.players = players
        self.size = size

    def satisfied(self, assignment: Dict[str, int]) -> bool:
        #print(f'ASSIGNMENT VALUES: {assignment.values()}')

        if len(assignment) < len(self.players):
            return True

        for pool in [1, 2, 3, 4]:

            poolCount = sum(1 for p in assignment.values() if p == pool)
            #print(poolCount)

            if poolCount != self.size:
                return False
        
        return True

'''
class PoolRequirementConstraint(Constraint[str, int]):
    def __init__(self, player: str, pool: int) -> None:
        super().__init__([player])
        self.player: str = player
        self.pool: int = pool

    def satisfied(self, assignment: Dict[str, int]) -> bool:
        # If either place is not in the assignment, then it is not
        # yet possible for their pools to be conflicting
        if self.player not in assignment:
            return True
        
        # check the pool assigned to place1 is not the same as the
        # pool assigned to place2
        return assignment[self.player] == [self.pool]
'''

def printResult(result):
    print(f"SOLUTION {solutionNumber}:")
    for pool in [1, 2, 3, 4]:
        poolPlayers = [player for player in result if result[player] == pool]

        print(f"---Pool {pool}---")

        for p in poolPlayers:
            print(p)

    print()

if __name__ == "__main__":
    players: List[str] = [
        "ALX R",
        "XIFL",
        "Poutine",
        "Thorn",
        "Mkok",
        "NerdCedric",
        "Kxmikaze",
        "Anaconda",
        "Rudulf",
        "Vermillion",
        "Walrus",
        "Yarkster",
        "Xozniath",
        "Brokensink",
        "5/Grim",
        "UT 2"
    ]

    pools: Dict[str, List[int]] = {}
    
    poolRestrictions = {
        "XIFL": 1,
        "Thorn": 2,
        "Kxmikaze": 3,
        "Poutine": 4
    }

    for player in players:

        try:
            pools[player] = [poolRestrictions[player]]

        except KeyError:
            pools[player] = [1, 2, 3, 4]

    csp: CSP[str, int] = CSP(players, pools)

    csp.add_constraint(PoolExclusionConstraint("Brokensink", "UT 2"))
    csp.add_constraint(PoolExclusionConstraint("Walrus", "Xozniath"))
    csp.add_constraint(PoolExclusionConstraint("Xozniath", "Thorn"))
    csp.add_constraint(PoolExclusionConstraint("Rudulf", "Vermillion"))
    csp.add_constraint(PoolExclusionConstraint("Poutine", "Yarkster"))
    csp.add_constraint(PoolExclusionConstraint("NerdCedric", "Kxmikaze"))

    csp.add_constraint(PoolSizeConstraint(players, 4))

    '''
    csp.add_constraint(PoolRequirementConstraint("XIFL", 1))
    csp.add_constraint(PoolRequirementConstraint("Thorn", 2))
    csp.add_constraint(PoolRequirementConstraint("Kxmikaze", 1))
    csp.add_constraint(PoolRequirementConstraint("Poutine", 1))
    '''

    print("Computing...")

    solutionNumber = 1

    solution: Optional[List[Dict[str, str]]] = csp.backtracking_search()
    
    if solution is []:
        print("No solution found!")
    else:
        printResult(solution)
        solutionNumber += 1