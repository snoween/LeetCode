class Solution:
    def maxScore(self, s: str) -> int:
        n = len(s)
        prefix_0 = [0] * n
        suffix_1 = [0] * n
        max_output = 0

        for i in range(n):
            prefix_0[i] = (prefix_0[i-1] if i > 0 else 0) + (1 if s[i] == '0' else 0)

        for i in range(n-1, -1, -1):
            suffix_1[i] = (suffix_1[i+1] if i < n-1 else 0) + (1 if s[i] == '1' else 0)
        
        for i in range(n-1):
            max_output = max(max_output, prefix_0[i] + suffix_1[i+1])
        
        return max_output