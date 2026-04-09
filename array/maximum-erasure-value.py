class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        best_sum = 0
        curr_sum = 0
        curr_num = set()
       
        l = 0
        for r, num in enumerate(nums):
            while num in curr_num:
                curr_num.remove(nums[l])
                curr_sum -= nums[l]
                l += 1
            
            curr_num.add(num)
            curr_sum += num

            best_sum = max(best_sum, curr_sum)
        
        return best_sum