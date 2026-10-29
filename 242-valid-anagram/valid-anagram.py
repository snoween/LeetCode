class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Solution: F2P
        """
        if len(s) != len(t):
            return False

        def CreateDict(string: str) -> dict:
            freq = {}
            for char in string:
                if char not in freq:
                    freq[char] = 0
                freq[char] += 1
            return freq
        
        freqS = CreateDict(s)
        freqT = CreateDict(t)
        for key, value in freqS.items():
            if key not in freqT:
                return False
            if value != freqT[key]:
                return False
        
        return True
