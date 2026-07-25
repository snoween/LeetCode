class Solution:
    def fib(self, n: int) -> int:
        def calculateFib(n):
            if n == 0:
                return 0
            elif n == 1:
                return 1
            else:
                return calculateFib(n - 2) + calculateFib(n - 1)
        
        return calculateFib(n)