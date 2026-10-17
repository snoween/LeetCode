class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        x_reversed = ''.join(list(reversed(str(x))))

        return True if int(x_reversed) == x else False