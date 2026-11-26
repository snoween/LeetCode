class Solution:
    def maxScore(self, s: str) -> int:
        """
        Solution: prefix sum
        - Calculate the prefix sum for left total (0's count only)
        - Calculate the suffix sum for right total (1's count only)
        - Get the maximum of prefix[i] + suffix[j] for i in range(0, n-1),
        j in range(1, n) 
        s = 0 1 1 1 0 1
        p = [1 1 1 1 2] 2
        s = 4 [4 3 2 1 1]
        max = p[0] + s[1] (because split the string -> offset by 1)
        """
        n = len(s)
        # calculate prefix
        prefix = [0] * n
        prefix[0] = int(s[0] == '0')
        for i in range(1, n):
            prefix[i] = prefix[i - 1] + int(s[i] == '0')
        
        # calculate suffix
        suffix = [0] * n
        suffix[-1] = int(s[-1] == '1')
        for j in range(n - 2, -1, -1):
            suffix[j] = suffix[j + 1] + int(s[j] == '1')
        
        max_val = 0
        for k in range(n - 1):
            max_val = max(max_val, prefix[k] + suffix[k + 1])
        
        return max_val