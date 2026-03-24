class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        j = 0
        count_cookies = 0
        
        s.sort()
        g.sort()

        for i in range(len(g)):               
            if j < len(s) and s[j] >= g[i]:
                count_cookies += 1
            j += 1
            
        return count_cookies