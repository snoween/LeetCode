class Solution:
    def countPoints(self, rings: str) -> int:
        rods = {i: set() for i in range(10)}

        for i in range(0, len(rings) - 1, 2):
            rods[int(rings[i + 1])].add(rings[i])

        count = 0
        for value in rods.values():
            if len(value) == 3:
                count += 1
        
        return count
