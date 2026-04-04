class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        current_sum = sum(nums[:k])
        ans = current_sum

        for right in range(k, len(nums)):
            current_sum = current_sum + nums[right] - nums[right - k]
            ans = max(ans, current_sum)
            
        return ans / k