class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        curr_sum = 0
        left = 0
        output = inf

        for right in range(len(nums)):
            curr_sum += nums[right]

            while curr_sum >= target:
                output = min(output, right-left+1)
                curr_sum -= nums[left]
                print(curr_sum)
                left += 1
                  
        return output if output != inf else 0