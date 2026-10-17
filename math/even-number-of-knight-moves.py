class Solution:
    def canReach(self, start: list[int], target: list[int]) -> bool:
        distance = (target[0] - start[0]) ** 2 + (target[1] - start[1]) ** 2
        
        if distance % 2 == 0:
            return True    
        return False