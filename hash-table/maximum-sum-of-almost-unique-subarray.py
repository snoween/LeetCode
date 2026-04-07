class Solution:
    def maxSum(self, nums: List[int], m: int, k: int) -> int:
        current_dict = Counter(nums[:k])
        current_sum = sum(nums[:k])
        
        max_sum = current_sum if len(current_dict.keys()) >= m else 0
        valid_array = False

        l = 0
        for r in range(k, len(nums)):  
            current_dict[nums[r]] += 1
            current_dict[nums[l]] -= 1
           
            if current_dict[nums[l]] == 0:      # Remove key if has dict[key] = 0
                del current_dict[nums[l]]

            current_sum = current_sum + nums[r] - nums[l]
            l += 1

            if len(current_dict.keys()) >= m:       
                max_sum = max(max_sum, current_sum)
                valid_aaray = True

        return max_sum if not valid_array else 0