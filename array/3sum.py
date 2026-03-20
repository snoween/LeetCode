class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        output = []
        l, r = 0, len(nums) - 1

        for i in range(len(nums) - 2):
            l = i + 1
            while l < r:
                if nums[l] + nums[r] == - nums[i]:
                    output.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                
                if nums[l] + nums[r] < - nums[i]:
                    r -= 1
                
                if nums[l] + nums[r] > - nums[i]:
                    l += 1
                    
            l, r = 0, len(nums) - 1
        print(output)

        return output
