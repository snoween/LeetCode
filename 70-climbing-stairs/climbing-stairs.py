class Solution:
    def climbStairs(self, n: int) -> int:
        """
        Solution: DP - bottom up
        - Base case: way(1) = 1, way(2) = 2
        - Formula: there are 2 ways to come to step i-th: way(i) = way(i - 1) + way(i - 2)
        - Time comp: O(N)
        - Space comp: O(1)
        """
        if n <= 2:
            return n
        
        oneStep = 2
        twoStep = 1
        for i in range(3, n + 1):
            currentStep = oneStep + twoStep
            twoStep = oneStep
            oneStep = currentStep

        return oneStep