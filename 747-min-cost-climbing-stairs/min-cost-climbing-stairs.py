class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        """
        Solution: DP - top down
        Base case: if there is less than 1 step -> can choose to move 2 steps or 0 step to get 0 cost
        Formula: There are 2 ways to move 1 or 2 steps -> choose the minimum cost to move
        ways[i] = min(ways[i - 1] + dp(i - 1), ways[i - 2] + dp(i - 2))
        """
        memo = {}

        def dp(steps):
            if steps <= 1:
                return 0
            
            if steps not in memo:
                moveOne = cost[steps - 1] + dp(steps - 1)
                moveTwo = cost[steps - 2] + dp(steps - 2)
                memo[steps] = min(moveOne, moveTwo)
            
            return memo[steps]
        
        return dp(len(cost))