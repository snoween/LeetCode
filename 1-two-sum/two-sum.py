class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Make a dictionary to pair num and its index
        num_idx = defaultdict(int)
        # make a list to append ans index
        ans = []
        # loop through list nums
        for i, num in enumerate(nums):
            curr_num = target - num
            # if target - curr_num in dict
            if curr_num in num_idx:
                # return (index curr_num, index target - curr_num)
                ans.extend([i, num_idx[curr_num]])
                return ans
            # if num not in dict -> add num to dict
            num_idx[num] = i

        