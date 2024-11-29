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
        
        # check the pool assigned to p1 is not the same as the
        # pool assigned to p2
        return assignment[self.p1] != assignment[self.p2]
    
class PoolRequirementConstraint(Constraint[str, str]):
    def __init__(self, p1: str, p2: str) -> None:
        super().__init__([p1, p2])
        self.p1: str = p1
        self.p2: str = p2

    def satisfied(self, assignment: Dict[str, str]) -> bool:
        # If either player is not in the assignment, then it is not
        # yet possible for their pools to be the same
        if self.p1 not in assignment or self.p2 not in assignment:
            return True
        
        # check the pool assigned to p1 is the same as the
        # pool assigned to place2
        return assignment[self.p1] == assignment[self.p2]

class PoolSizeConstraint(Constraint[str, int]):
    def __init__(self, players: List[str], size: int) -> None:
        super().__init__(players)
        self.players = players
        self.size = size

    def satisfied(self, assignment: Dict[str, int]) -> bool:

        if len(assignment) < len(self.players):
            return True

        for pool in [1, 2, 3, 4]:

            poolCount = sum(1 for p in assignment.values() if p == pool)

            if poolCount != self.size:
                return False
        
        return True

#pretty-prints final pool(s) in table form
def printResult(result):

    template = "|{0:12}|{1:12}|{2:12}|{3:12}|" # column widths: 8, 10, 15, 7, 10

    finalPools = {}
    for pool in [1, 2, 3, 4]:
        finalPools[pool] = [player for player in result if result[player] == pool]

    print(f"\nSOLUTION #{solutionNumber}:")

    print(template.format("Pool 1", "Pool 2", "Pool 3", "Pool 4"))
    print("-" * 53)

    for p in range(poolSize):
        print(template.format(finalPools[1][p], finalPools[2][p], finalPools[3][p], finalPools[4][p]))

if __name__ == "__main__":
    players: List[str] = [
        "ALX R",
        "XIFL",
        "Poutine",
        "Thorn",
        "Mkok",
        "Stxr",
        "NerdCedric",
        "Kxmikaze",
        "Anaconda",
        "Rudulf",
        "Lars",
        "Vermillion",
        "Aynim",
        "Walrus",
        "Yarkster",
        "Tepig",
        "NickSF",
        "Xozniath",
        "Ween",
        "Brokensink",
        "Grimturtle",
        "Tavares",
        "Mork",
        "Toadrex"
    ]

    #Determines the size of the pools
    poolSize = 6

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

    csp.add_constraint(PoolSizeConstraint(players, poolSize))

    #########################
    ### USER CONSTRAINTS: ###
    #########################

    #EXTREMELY IMPORTANT CONFLICTS TO AVOID
    csp.add_constraint(PoolExclusionConstraint("NickSF", "Stxr"))
    csp.add_constraint(PoolExclusionConstraint("Brokensink", "Toadrex"))
    csp.add_constraint(PoolExclusionConstraint("Walrus", "Xozniath"))
    csp.add_constraint(PoolExclusionConstraint("Xozniath", "Thorn"))
    csp.add_constraint(PoolExclusionConstraint("Aynim", "Lars"))
    csp.add_constraint(PoolExclusionConstraint("Rudulf", "Vermillion"))
    csp.add_constraint(PoolExclusionConstraint("Poutine", "Yarkster"))
    csp.add_constraint(PoolExclusionConstraint("Tavares", "Mork"))
    csp.add_constraint(PoolExclusionConstraint("Tepig", "Ween"))
    csp.add_constraint(PoolExclusionConstraint("NerdCedric", "Kxmikaze"))
    
    #Frequent / recent opponents, nice to avoid
    csp.add_constraint(PoolExclusionConstraint("Poutine", "Walrus"))
    csp.add_constraint(PoolExclusionConstraint("Walrus", "Yarkster"))
    csp.add_constraint(PoolExclusionConstraint("Thorn", "Yarkster"))
    csp.add_constraint(PoolExclusionConstraint("Thorn", "Walrus"))
    csp.add_constraint(PoolExclusionConstraint("ALX R", "XIFL"))

    csp.add_constraint(PoolExclusionConstraint("Brokensink", "NerdCedric"))
    
    csp.add_constraint(PoolExclusionConstraint("Thorn", "Lars"))
    csp.add_constraint(PoolExclusionConstraint("Brokensink", "NerdCedric"))
    csp.add_constraint(PoolExclusionConstraint("Brokensink", "NickSF"))
    csp.add_constraint(PoolExclusionConstraint("XIFL", "Mkok"))
    csp.add_constraint(PoolExclusionConstraint("XIFL", "NickSF"))
    csp.add_constraint(PoolExclusionConstraint("XIFL", "Yarkster"))
    csp.add_constraint(PoolExclusionConstraint("Tavares", "NickSF"))
    csp.add_constraint(PoolExclusionConstraint("Poutine", "NickSF"))
    csp.add_constraint(PoolExclusionConstraint("Walrus", "Mkok"))

    #Sets we would prefer to avoid
    csp.add_constraint(PoolExclusionConstraint("Stxr", "Lars"))
    csp.add_constraint(PoolExclusionConstraint("Stxr", "Rudulf"))
    csp.add_constraint(PoolExclusionConstraint("Rudulf", "Lars"))

    csp.add_constraint(PoolExclusionConstraint("XIFL", "Aynim"))
    csp.add_constraint(PoolExclusionConstraint("Rudulf", "XIFL"))
    csp.add_constraint(PoolExclusionConstraint("Rudulf", "Aynim"))

    csp.add_constraint(PoolExclusionConstraint("Thorn", "NerdCedric"))
    csp.add_constraint(PoolExclusionConstraint("Stxr", "Anaconda"))
    csp.add_constraint(PoolExclusionConstraint("ALX R", "Lars"))
    csp.add_constraint(PoolExclusionConstraint("ALX R", "Walrus"))
    csp.add_constraint(PoolExclusionConstraint("XIFL", "NickSF"))
    csp.add_constraint(PoolExclusionConstraint("ALX R", "NickSF"))
    
    csp.add_constraint(PoolExclusionConstraint("Anaconda", "Mkok"))

    #Hot sets! We WANT these to happen!
    csp.add_constraint(PoolRequirementConstraint("Poutine", "Lars"))
    csp.add_constraint(PoolRequirementConstraint("Stxr", "Kxmikaze"))
    csp.add_constraint(PoolRequirementConstraint("Ween", "Vermillion"))
    csp.add_constraint(PoolRequirementConstraint("Tepig", "Mkok"))

    print("Computing valid pools...")

    solutionNumber = 1

    csp.backtracking_search()
    solution: Optional[List[Dict[str, str]]] = csp.solutions
    
    if solution is []:
        print("No solution(s) found!")
    else:
        for s in solution:
            printResult(s)
            solutionNumber += 1