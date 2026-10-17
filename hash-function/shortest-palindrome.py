class Solution:
    def shortestPalindrome(self, s: str) -> str:
        char_map = {chr(ord('a') + i): i for i in range(26)}

        longest_palin =  ''
        forward, backward = 0, 0
        num = 1

        for i, char in enumerate(s):
            forward = forward * 26 + char_map[char] 
            backward += char_map[char] * num
            num *= 26

            if forward == backward:
                longest_palin = s[:i+1]

        if len(longest_palin) < len(s):
            add_text = s[len(longest_palin):] 
            return add_text[::-1] + s
        
        return longest_palin