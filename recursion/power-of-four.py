class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        def calculatePower(num):
            if n == num or n == 1:
                return True
            elif n < num:
                return False
            else:
                return calculatePower(num * 4)
        
        return calculatePower(4)