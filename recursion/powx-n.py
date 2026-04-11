class Solution:
    def myPow(self, x: float, n: int) -> float:
        output = 1
        for i in range(abs(n)):
            output *= x
        return output if n > 0 else 1/output