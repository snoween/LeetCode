class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Make negative list
        stones_negative = [-num for num in stones]
        # heapify the list
        heapq.heapify(stones_negative)
        # while len negative arr > 1
        while len(stones_negative) > 1:
            # pop 1st stone
            stone1 = heapq.heappop(stones_negative)
            # pop 2nd stone
            stone2 = heapq.heappop(stones_negative)
            # if stone 1 != stone 2
            if stone1 != stone2:
                # heap push -abs((stone 1 - stone 2)) -> negative array
                heapq.heappush(stones_negative, -abs(stone1 - stone2))
        
        # return -negative[0] else 0
        return -stones_negative[0] if stones_negative else 0
            
        