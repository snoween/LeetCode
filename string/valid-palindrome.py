class Solution:
    def isPalindrome(self, s: str) -> bool:
        # set left, right pointer at 2 heads of array
        left = 0
        right = len(s) - 1

        # while loop if left < right
        while left < right:
            if not s[left].isalnum():
                left += 1
            elif not s[right].isalnum():
                right -= 1
            elif s[left].lower() != s[right].lower():
                return False
            else:
                left += 1
                right -= 1
        
        return True

            
            
        
        # return True
        return True
            
