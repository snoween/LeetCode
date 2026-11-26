class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        """
        Solution: prefix sum
        - if left sum = right sum and separate by nums[i]
        -> number at index i separates the list into 2 parts that have same sum
        -> left_sum + nums[i] = right_sum + nums[i]
        -> prefix[i] = suffix[i]
        - Check if prefix[i] = suffix[i] -> return i
        """
        n = len(nums)

        prefix = nums[:]
        for i in range(1, n):
            prefix[i] += prefix[i - 1]
        
        suffix = nums[:]
        for j in range(n - 2, -1, -1):
            suffix[j] += suffix[j + 1]
        
        for k in range(n):
            if prefix[k] == suffix[k]:
                return k
        
        return -1

