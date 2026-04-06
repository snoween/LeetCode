class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        seen_arr = set()
        current_sum = 0
        max_sum = 0
        l = 0

        for r, num in enumerate(nums):
            while num in seen_arr:
                seen_arr.remove(nums[l])
                current_sum -= nums[l]
                l += 1

            seen_arr.add(num)    
            current_sum += num
            max_sum = max(max_sum, current_sum)
        
        return max_sum