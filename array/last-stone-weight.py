class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # heap -> [-8 -7 -4 -2 -1 -1] 
        # First iteration
            # Pop x2: (-8) - (-7) = -1
            # Push --> [-4 -2 -1 -1 -1]
        # Second iteration
            # Pop x2: (-4) - (-2) = -2
            # Push --> [-2 -1 -1 -1]
        stones_minus = [-num for num in stones]
        heapq.heapify(stones_minus)

        while len(stones_minus) > 1:
            element1 = heapq.heappop(stones_minus)
            element2 = heapq.heappop(stones_minus)
            diff = element1 - element2

            if diff != 0:
                heapq.heappush(stones_minus, diff)
        
        return -stones_minus[0]