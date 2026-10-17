class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        moveTwo = 0
        moveOne = 0

        n = len(cost)
        for i in range(2, n + 1):
            curr = min(moveOne + cost[i - 1], moveTwo + cost[i - 2])

            # update movement for next loop
            moveTwo = moveOne
            moveOne = curr
        
        return moveOne