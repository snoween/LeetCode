class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()

        result = []

        for a in range(len(nums)):
            if a > 0 and nums[a] == nums[a-1]:
                continue
            for b in range(a+1, len(nums)):
                if b > a + 1 and nums[b] == nums[b-1]:
                    continue

                d = len(nums) - 1
                for c in range(b + 1, len(nums)):
                    if c > b + 1 and nums[c] == nums[c-1]:
                        continue

                    while c < d and nums[a] + nums[b] + nums[c] + nums[d] > target:
                        d -= 1
                    
                    if c < d and nums[a] + nums[b] + nums[c] + nums[d] == target:
                        result.append([nums[a], nums[b], nums[c], nums[d]])

        return result