class Solution:
    def climbStairs(self, n: int) -> int:
        """
        Solution: DP - bottom up
        Base case: when have less than 2 steps -> return it, 1 step has 1 way, 2 steps = 2 ways (move 1->1 step, or move 2 steps)
        Formula: there are 2 ways to move to step i-th: move 1 step or 2 steps
        ways(i) = way(i - 1) + ways(i - 2)
        """

        if n <= 2:
            return n
        
        moveOne = 1
        moveTwo = 2

        for i in range(3, n + 1):
            current = moveOne + moveTwo

            moveOne = moveTwo
            moveTwo = current
        
        return moveTwo