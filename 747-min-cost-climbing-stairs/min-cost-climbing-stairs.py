class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        """
        Solution: DP - bottom up
        Base case: if there is less than 1 step -> can choose to move 2 steps or 0 step to get 0 cost
        Formula: There are 2 ways to move 1 or 2 steps -> choose the minimum cost to move
        ways[i] = min(ways[i - 1] + dp(i - 1), ways[i - 2] + dp(i - 2))
        """
        n = len(cost)
        dp = [0] * (n + 1)
        for i in range(2, n + 1):
            dp[i] = min(cost[i - 1] + dp[i - 1], cost[i - 2] + dp[i - 2])
        
        return dp[-1]