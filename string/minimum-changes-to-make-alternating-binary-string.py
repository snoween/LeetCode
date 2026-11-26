class Solution:
    def minOperations(self, s: str) -> int:
        count_zero = 0

        # start with 0 -> str will be 0101
        for i in range(len(s)):
            if i % 2 == 0 and s[i] != '0':
                count_zero += 1
            elif i % 2 != 0 and s[i] != '1':
                count_zero += 1
        
        count_one = len(s) - count_zero
        return min(count_zero, count_one)