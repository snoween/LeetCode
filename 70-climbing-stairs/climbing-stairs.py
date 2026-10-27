class Solution:
    def climbStairs(self, n: int) -> int:
        """
        Solution: DP - top down
        - Base case: way(1) = 1, way(2) = 2
        - Formula: there are 2 ways to come to step i-th: way(i) = way(i - 1) + way(i - 2)
        - Time comp: O(N)
        - Space comp: O(N)
        """
        memo = {}

        def dp(step):
            if step == 1:
                return 1
            if step == 2:
                return 2
            
            if step in memo:
                return memo[step]
            
            memo[step] = dp(step - 1) + dp(step - 2)
            return memo[step]
        
        return dp(n)