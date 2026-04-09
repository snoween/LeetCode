class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        l = 0
        curr_prod = nums[0]
        count = 1 if curr_prod < k else 0

        for r in range(1, len(nums)):
            curr_prod *= nums[r]
            while curr_prod >= k and l <= r:
                print(curr_prod)
                curr_prod = curr_prod // nums[l]
                l += 1
            
            if curr_prod < k:
                print(r, l, count, curr_prod)
                count += (r-l+1)
                print(count)

        
        return count



