class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        best_sum, best_dist = 0, float('inf')

        for i in range(len(nums)):
            j, k = i + 1, len(nums) - 1
            while j < k:
                init_sum = nums[i] + nums[j] + nums[k]
                init_dist = abs(init_sum - target)

                if nums[i] + nums[j] + nums[k] > target:
                    k -= 1
                
                elif nums[i] + nums[j] + nums[k] == target:
                    return target
                
                else:
                    j += 1
                
                if init_dist < best_dist:
                    best_dist = init_dist
                    best_sum = init_sum
        
        return best_sum
                
                

