class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0
        res = []
        n = min(len(word1), len(word2))
        
        while i < n:
            res.append(word1[i])
            res.append(word2[i])
            i += 1
        
        res.extend(word1[i::])
        res.extend(word2[i::])

        return ''.join(res)
