class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        num_triangle = 0

        for i in range(len(nums)):
            k = i + 2
            for j in range(i + 1, len(nums)):
                while k < len(nums) and nums[i] + nums[j] > nums[k]:
                    k += 1
                
                num_triangle += max(0, (k - 1) - j)
        
        return num_triangle
