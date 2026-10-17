class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        Solution: 2 pointers
        Time comp: O(N)
        Space comp: O(1)
        """
        left, right = 0, len(s) - 1

        while left < right:
            if not s[left].isalnum():
                left += 1
            elif not s[right].isalnum():
                right -= 1
            else:
                if s[left].lower() == s[right].lower():
                    left += 1
                    right -= 1
                else:
                    return False
        
        return True