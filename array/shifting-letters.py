class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        char_dict = {chr(ord('a') + i): i for i in range(26)}
        n = len(shifts)
        suffix = [0] * n
        output = []
        mod = 26

        for i in range(n-1, -1, -1):
            suffix[i] = (suffix[i+1] if i < n-1 else 0) + shifts[i]

        for i in range(n):
            suffix[i] = ((suffix[i] % mod) + char_dict[s[i]]) % mod
                
            for key, val in char_dict.items():
                if suffix[i] == val:
                    output.append(key)
        
        return ''.join(output)
        
