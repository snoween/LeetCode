class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        l = 0
        seen = set()
        best_sum = 0
        sum_subarray = 0
        for r, num in enumerate(nums):
            
            while num in seen:
                seen.remove(nums[l])
                sum_subarray -= nums[l]
                l += 1

            sum_subarray += num
            seen.add(num)

            best_sum = max(best_sum, sum_subarray)
        
        return best_sum

