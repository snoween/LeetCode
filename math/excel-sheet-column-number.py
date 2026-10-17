class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        ans = 0
        n = len(columnTitle)
        for i in range(n - 1, -1, -1):
            ans += (ord(columnTitle[i]) - ord('A') + 1) * (26 ** (n - i - 1))
    
        return ans 