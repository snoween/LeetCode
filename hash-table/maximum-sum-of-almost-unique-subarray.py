class Solution:
    def maxSum(self, nums: List[int], m: int, k: int) -> int:
        current_dict = Counter(nums[:k])
        l = 0
        current_sum = 0 if len(current_dict.keys()) < m else sum(nums[:k])
        max_sum = current_sum

        for r in range(k, len(nums)):
            current_dict[nums[r]] += 1
            current_dict[nums[l]] -= 1

            if current_dict[nums[l]] == 0:
                del current_dict[nums[l]]

            if len(current_dict.keys()) >= m:    
                current_sum = current_sum + nums[r] - nums[l]
                l += 1
                max_sum = max(max_sum, current_sum)

            else:
                current_sum = current_sum + nums[r] - nums[l]
                l += 1

        return max_sum