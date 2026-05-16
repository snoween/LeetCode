class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        seen = set()
        target = 0
        output = []
        # for loop i
        for i, num in enumerate(nums):
            # check if target in set seen or not
            if num in seen:
                continue
            else:
                seen.add(num)
                target = num
            
            # Set up l, r
            l = i+1
            r = len(nums) - 1
            
            while l < r:
                print(target, nums[l], nums[r])
                if nums[l] + nums[r] + target == 0:
                    output.append([target, nums[l], nums[r]])
                
                l += 1
                r -= 1
        
        return output