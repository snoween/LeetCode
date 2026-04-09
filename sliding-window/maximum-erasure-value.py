class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        best_sum = 0
        curr_sum = 0
        curr_num = set()
       
        l = 0
        for r in range(len(nums)):
            while nums[r] in curr_num:
                curr_num.remove(nums[l])
                curr_sum -= nums[l]
                l += 1
            
            curr_num.add(nums[r])
            curr_sum += nums[r]

            best_sum = max(best_sum, curr_sum)
        
        return best_sum