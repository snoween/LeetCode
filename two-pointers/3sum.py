class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        seen = set()
        target = 0
        output_seen = set()
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
                if nums[l] + nums[r] > -target:
                    r -= 1

                elif nums[l] + nums[r] < -target:
                    l += 1
                
                else:
                    if tuple([target, nums[l], nums[r]]) not in output_seen:
                        output.append([target, nums[l], nums[r]])
                    output_seen.add(tuple([target, nums[l], nums[r]]))
                    r -= 1
                    l += 1
        
        return output