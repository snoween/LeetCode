class Solution:
    def climbStairs(self, n: int) -> int:
        """
        Solution: DP - top down
        Base case: when have less than 2 steps -> return it, 1 step has 1 way, 2 steps = 2 ways (move 1->1 step, or move 2 steps)
        Formula: there are 2 ways to move to step i-th: move 1 step or 2 steps
        ways(i) = way(i - 1) + ways(i - 2)
        """
        memo = {}

        def dp(steps):
            if steps <= 2:
                return steps
            if steps not in memo:
                memo[steps] = dp(steps - 1) + dp(steps - 2)
            
            return memo[steps]
        
        return dp(n)