class Solution:
    def maxScore(self, s: str) -> int:
        n = len(s)
        prefix = [0] * n
        suffix = [0] * n
        max_sum = 0

        # Get sum of prefix 
        for i in range(n-1):

            prefix[i] = (prefix[i-1] if i > 0 else 0) + int(s[i] == '0')
        
        for j in range(n-1, 0, -1):
            suffix[j] = (suffix[j+1] if j < n-1 else 0) + int(s[j] == '1')
        
        print(prefix, suffix)
        for i in range(n):
            max_sum = max(max_sum, prefix[i] + suffix[i])
        
        return max_sum
