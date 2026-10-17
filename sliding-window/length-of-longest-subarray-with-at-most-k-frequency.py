class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        freq = Counter()
        max_len = 0

        left = 0
        for right, num in enumerate(nums):
            freq[num] += 1

            while freq[num] > k:
                freq[nums[left]] -= 1
                left += 1
            
            max_len = max(max_len, right-left+1)
        
        return max_len