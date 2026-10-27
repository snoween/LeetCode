class Solution:
    def climbStairs(self, n: int) -> int:
        """
        Solution: DP - bottom up
        - Base case: way(1) = 1, way(2) = 2
        - Formula: there are 2 ways to come to step i-th: way(i) = way(i - 1) + way(i - 2)
        - Time comp: O(N)
        - Space comp: O(N)
        """
        if n <= 2:
            return n
        
        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        
        return dp[-1]
