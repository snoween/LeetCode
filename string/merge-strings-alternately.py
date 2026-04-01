class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0
        res = ''
        n = min(len(word1), len(word2))
        
        while i < n:
            res += word1[i]
            res += word2[i]
            i += 1
        
        res += word1[i::]
        res += word2[i::]

        return res
