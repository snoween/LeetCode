class Solution:
    def fib(self, n: int) -> int:
        """
        Solution: DP - bottom up
        - Base case: fib(0) = 0, fib(1) = 1
        - Formula: fib(i) = fib(i - 1) + fib(i - 2)
        - Time comp: O(N)
        - Space comp: O(N)
        """
        
        if n == 0:
            return 0
        if n == 1:
            return 1
        
        dp = [0] * (n + 1)
        dp[1] = 1
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        
        return dp[-1]
