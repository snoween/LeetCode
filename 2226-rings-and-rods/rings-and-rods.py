class Solution:
    def countPoints(self, rings: str) -> int:
        rods = {i: [0, 0, 0] for i in range(10)}

        for i in range(0, len(rings) - 1, 2):
            value = rods[int(rings[i + 1])]
            if rings[i] == 'R':
                value[0] += 1
            elif rings[i] == 'G':
                value[1] += 1
            else:
                value[2] += 1
        
        count = 0
        for value in rods.values():
            if 0 not in value:
                count += 1
        
        return count
