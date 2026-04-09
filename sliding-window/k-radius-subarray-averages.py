class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        if k == 0:
            return nums
        elif len(nums) < k:
            return [-1 for _ in range(len(nums))]

        output = [-1 for _ in range(len(nums))]
        curr_sum = sum(nums[:2*k+1])
        output[k] = curr_sum // (2*k + 1)

        for r in range(k+1, len(nums)-k):
           
            curr_sum = curr_sum + nums[r + k] - nums[r - k - 1]
            output[r] = curr_sum // (2*k + 1)

            
            
        
        return output
