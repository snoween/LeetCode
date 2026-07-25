class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        def calculatePower(num):
            if n == num or n == 1:
                return True
            elif n < num:
                return False
            elif n > num:
                return calculatePower(num * 3)
        
        return calculatePower(3)