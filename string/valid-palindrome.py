class Solution:
    def isPalindrome(self, s: str) -> bool:
        # set left, right pointer at 2 heads of array
        left = 0
        right = len(s) - 1

        # while loop if left < right
        while left < right:
            # while left is not alpha -> move left
            while not s[left].isalpha():
                left += 1

            # while right is not alpha -> move right
            while not s[right].isalpha():
                right -= 1

            # if left lower != right lower
            if s[left].lower() != s[right].lower():
                # return false
                return False
            
            # move left right
            left += 1
            right -= 1
        
        # return True
        return True
            
