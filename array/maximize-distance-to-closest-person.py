class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        first_1_idx = 0
        dist = 0
        position = 0

        # Find the first 1 idx
        for i, num in enumerate(seats):
            if num == 1:
                first_1_idx = i
                break
        
        for i in range(first_1_idx, len(seats)):
            if seats[i] == 1:
                max_dist = i - first_1_idx
                if max_dist > dist:
                    position = max_dist // 2
                    dist = max_dist
                    first_1_idx = i
        
        if position == 0:
            position = len(seats) - 1
        
        return position
