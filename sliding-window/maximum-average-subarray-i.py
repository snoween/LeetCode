class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        curr_sum = sum(nums[:k])
        max_avg = curr_sum / k
        left = 0

        for right in range(k, len(nums)):
            curr_sum = curr_sum - nums[left] + nums[right]
            left += 1

            max_avg = max(max_avg, curr_sum/k)
        
        return max_avg