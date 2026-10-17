class Solution:
    def romanToInt(self, s: str) -> int:
        rom_val = {"I": 1,
                    "V": 5,
                    "X": 10,
                    "L": 50,
                    "C": 100,
                    "D": 500,
                    "M": 1000}
        ans = 0
        prev_char = s[0]

        for char in s:
            if rom_val[char] > rom_val[prev_char]:
                ans = ans - rom_val[prev_char] * 2
            prev_char = char
            ans += rom_val[char]
        
        return ans