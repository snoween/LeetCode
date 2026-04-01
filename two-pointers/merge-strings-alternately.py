class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ''
        
        for i in range(min(len(word1), len(word2))):
            res += word1[i]
            res += word2[i]
            
        if len(word1) != len(word2):
            j = abs(len(word2) - len(word1))
            res += word1[j::]
            res += word2[j::]

        return res
