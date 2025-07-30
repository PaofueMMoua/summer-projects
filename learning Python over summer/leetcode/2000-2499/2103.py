class Solution:
    def countPoints(self, rings: str) -> int:
    
        rods = {}
        for i in range(0, len(rings), 2):
            rods[rings[i:i+2][1]] = rods.get(rings[i:i+2][1], set())
            rods[rings[i:i+2][1]].add(rings[i:i+2][0])
        return sum([1 for i in rods.values() if len(i) == 3])