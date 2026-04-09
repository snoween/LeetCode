class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        curr_prod = nums[0]
        count = 1 if curr_prod < k else 0
        
        l = 0
        for r in range(1, len(nums)):
            curr_prod *= nums[r]        # Update

            while curr_prod >= k and l <= r:        # Check how to change the size of curr window
                curr_prod = curr_prod // nums[l]
                l += 1

            count += (r-l+1)

        return count