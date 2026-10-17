class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        list_s = list(s)
        left = 0
        right = len(s) - 1

        while left < right:
            if list_s[left].isalpha() and list_s[right].isalpha():
                list_s[left], list_s[right] = list_s[right], list_s[left]
                left += 1
                right -= 1
            elif not list_s[right].isalpha():
                right -= 1
            elif not list_s[left].isalpha():
                left += 1
        
        return ''.join(list_s)