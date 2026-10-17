class Solution:
    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return self.validate(s, left + 1, right) or self.validate(s, left, right - 1)

        return True
        
    def validate(self, s, left, right):
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        
        return True