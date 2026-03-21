class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        count = 0
        nums.sort()
        first_0_idx = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                first_0_idx = i
                break
        
        k = first_0_idx + 2

        for i in range(first_0_idx, len(nums) - 2):
            if k > len(nums) - 1:
                k = len(nums) - 1

            for j in range(i+1, len(nums) - 1):
                if j != k:
                    while k < len(nums) and nums[i] + nums[j] > nums[k]:
                        print(nums[i], nums[j], nums[k])
                        k += 1
                    
                    count += k - j - 1

        return count