class Solution:
    def sumOddLengthSubarrays(self, arr: list[int]) -> int:
        n = len(arr)
        prefix = [0] * n
        prefix[0] = arr[0]

        for i in range(1, n):
            prefix[i] = prefix[i - 1] + arr[i]
        
        total = 0
        for left in range(n):
            for right in range(left, n, 2):
                if left == 0:
                    total += prefix[right]
                else:
                    total += (prefix[right] - prefix[left - 1])
        
        return total