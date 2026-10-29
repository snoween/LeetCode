class Solution:
    def fib(self, n: int) -> int:
        """
        Solution: DP - top down
        - Base case: fib(0) = 0, fib(1) = 1
        - Formula: fib(i) = fib(i - 1) + fib(i - 2)
        - Time comp: O(N)
        - Space comp: O(N)
        """
        if n <= 1:
            return n

        prevOne = 1
        prevTwo = 0
        for i in range(2, n + 1):
            current = prevTwo + prevOne
            prevTwo = prevOne
            prevOne = current
        
        return prevOne