class Solution:
    def maxScore(self, s: str) -> int:
        n = len(s)
        prefix = [0] * n
        suffix = [0] * n
        max_sum = 0

        # Get sum of prefix 
        for i in range(n):
            prefix[i] = (prefix[i-1] if i > 0 else 0) + int(s[i] == '0')
        
        for j in range(n-1, -1, -1):
            suffix[j] = (suffix[j+1] if j < n-1 else 0) + int(s[j] == '1')
        
        # Prefix runs from [0, n - 2] - no need the last ele
        # Suffix funs from [1, n - 1] - no need the first ele
        for i in range(n-1):
            max_sum = max(max_sum, prefix[i] + suffix[i+1])
        
        return max_sum