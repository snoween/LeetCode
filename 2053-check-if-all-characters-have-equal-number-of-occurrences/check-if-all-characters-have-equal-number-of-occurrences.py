class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        freq = Counter(s)
        target = freq[s[0]]

        if len(freq) == 1:
            return True
        
        for val in freq.values():
            if val != target:
                return False
        
        return True