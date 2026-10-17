class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        k = 0
        count = 0

        while k < len(nums):
            count_k = 0
            for num in nums:
                if abs(num - nums[k]) == diff:
                    count_k += 1

            if count_k == 2:
                count += 1
                
            k += 1
        
        return count