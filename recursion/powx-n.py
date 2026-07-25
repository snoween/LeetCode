class Solution:
    def myPow(self, x: float, n: int) -> float:
        def calculatePow(num, n):
            if n == 0:
                return num
            elif n > 0:
                return calculatePow(num * x, n - 1)
            elif n < 0:
                return calculatePow(num * x, n + 1)
        if n > 0:
            return calculatePow(x, n) / x
        else:
            return (1 / calculatePow(x, n)) * x