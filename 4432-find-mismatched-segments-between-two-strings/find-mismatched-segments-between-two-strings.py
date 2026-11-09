class Solution:
    def findMismatchedSegments(self, s1: str, s2: str) -> list[list[str]]:
        """
        Solution: brute force
        - Have 2 lists to store different characters
        - Renew those lists to empty lists if meet the same characters
        """
        str1, str2 = [], []
        result = []

        for c1, c2 in zip(s1, s2):
            if c1 != c2:
                str1.append(c1)
                str2.append(c2)
            else:
                if str1:
                    result.append([''.join(str1), ''.join(str2)])
                    str1, str2 = [], []
        
        if str1:    # in case there is no different characters
            result.append([''.join(str1), ''.join(str2)])
        
        return result