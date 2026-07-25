class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        def powerthree(num):
            if n == num:
                return True
            elif n < num:
                return False
            elif n > num:
                return powerthree(num * 3)
        
        return powerthree(3)
        