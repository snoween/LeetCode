class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Time comp: O(N)
        Space comp: O(N)
        Method: hashmap
        """
        num_idx = defaultdict(int)

        for i, curr in enumerate(nums):
            # Calculate the difference
            diff = target - curr
            if num_idx and diff in num_idx:
                return [num_idx[diff], i]
            num_idx[curr] = i