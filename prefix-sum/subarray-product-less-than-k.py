class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        count = 0
        l = 0
        curr_prod = nums[0]
        for r in range(len(nums)):
            while curr_prod > k and l < len(nums):
                curr_prod = curr_prod / nums[l]
                l += 1
            
            curr_prod *= nums[r]
            count += (r-l+1)
        
        return count if count > 0 else 0



