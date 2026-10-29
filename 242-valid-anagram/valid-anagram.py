class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Solution: F2P
        """
        if len(s) != len(t):
            return False

        freqS = {}
        freqT = {}

        for charS in s:
            if charS not in freqS:
                freqS[charS] = 0
            freqS[charS] += 1
        
        for charT in t:
            if charT not in freqT:
                freqT[charT] = 0
            freqT[charT] += 1
        
        for key, value in freqS.items():
            if key not in freqT:
                return False
            if value != freqT[key]:
                return False
        
        return True
