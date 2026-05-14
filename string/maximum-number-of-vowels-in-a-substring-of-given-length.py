class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowel = set('aeiou')
        vowelCount = 0
        for i in range(k):
            if s[i] in vowel:
                vowelCount += 1

        max_count = vowelCount
        
        for i in range(k, len(s)):
            if s[i-k] in vowel:
                vowelCount -= 1
                
            if s[i] in vowel:
                vowelCount += 1
        
            max_count = max(max_count, vowelCount)
        
        return max_count