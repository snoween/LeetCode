class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        count = 0
        for i, num in enumerate(s):
            count += int(count < len(g) and num >= g[count])
        
        return count