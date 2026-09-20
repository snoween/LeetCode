class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set('aeiou')
        count = 0

        for i in range(k):
            if s[i] in vowels:
                count += 1
        
        max_count = count

        for j in range(k, len(s)):
            if s[j] in vowels:  # check right char
                count += 1
            if s[j - k] in vowels:  # check left char
                count -= 1
            max_count = max(max_count, count)
        
        return max_count