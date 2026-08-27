class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        - Time comp: O(N)
        - Space comp: O(N)
        - Idea: use dict to save seen num with its index. Loop through
        array, if target - curr_num in dict -> return index of both old + curr num
        """

        seen = defaultdict(int)

        for i, curr_num in enumerate(nums):
            diff = target - curr_num

            if diff in seen:
                return [i, seen[diff]]

            seen[curr_num] = i