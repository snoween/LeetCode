class Solution:
    def maxSum(self, nums: List[int], m: int, k: int) -> int:
        current_dict = Counter(nums[:k])
        l = 0
        current_sum = sum(nums[:k])
        max_sum = current_sum
        max_m = len(current_dict.keys())

        for r in range(k, len(nums)):
            
            current_dict[nums[r]] += 1
            current_dict[nums[l]] -= 1
           
            if current_dict[nums[l]] == 0:
                del current_dict[nums[l]]
            max_m = max(max_m, len(current_dict.keys()))
               
            if len(current_dict.keys()) >= m:    
                print(current_sum, nums[r], nums[l])
                current_sum = current_sum + nums[r] - nums[l]
                l += 1
                max_sum = max(max_sum, current_sum)

            else:
                current_sum = current_sum + nums[r] - nums[l]
                l += 1

        return max_sum if max_m >= m else 0