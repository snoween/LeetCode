class Solution:
    def isPalindrome(self, s: str) -> bool:
        # set left, right pointer at 2 heads of array
        left = 0
        right = len(s) - 1

        # while loop if left < right
        while left < right:
            # if left is not alnum -> increase left
            if not s[left].isalnum():
                left += 1
            # elif right is not alnum -> decrease right
            elif not s[right].isalnum():
                right -= 1
            # if both are alnum but not same value -> return false
            elif s[left].lower() != s[right].lower():
                return False
            # if both are alnum and same values -> move left right
            else:
                left += 1
                right -= 1
        
        return True