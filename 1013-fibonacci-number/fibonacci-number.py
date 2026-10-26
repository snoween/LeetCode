class Solution:
    def fib(self, n: int) -> int:
        """
        Solution: DP - top down
        - Base case: fib(0) = 0, fib(1) = 1
        - Formula: fib(i) = fib(i - 1) + fib(i - 2)
        - Time comp: O(N)
        - Space comp: O(N)
        """
        memo = {}
        
        def dp(num):
            if num == 0:
                return 0
            if num == 1:
                return 1
            if num in memo:
                return memo[num]

            memo[num] = dp(num - 1) + dp(num - 2)
            return memo[num]
        
        return dp(n)