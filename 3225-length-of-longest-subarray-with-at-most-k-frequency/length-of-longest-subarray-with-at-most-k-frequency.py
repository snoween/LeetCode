class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        max_len = 0
        freq = defaultdict(int)
        l = 0

        for r, num in enumerate(nums):           
            freq[num] += 1
            
            while freq[num] > k:
                freq[nums[l]] -= 1

                if freq[nums[l]] == 0:
                    del freq[nums[l]]
                l += 1
            
            max_len = max(max_len, r-l+1)
    
        return max_len