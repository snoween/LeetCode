class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        """
        Solution: Binary search
        - Index of a pair always starts at even idx, ends at odd idx
        -> Check if mid is odd or even, compare with mid - 1 or mid + 1
        -> return if mid is not equal to mid-1/mid+1
        """
        left, right = 0, len(nums) - 1

        while left < right:
            middle = left + (right - left) // 2

            # check if half left has single num
            if middle % 2 == 0:
                if nums[middle] == nums[middle + 1]:
                    left = middle + 2
                else:
                    right = middle
            else:   # in case single num in half right -> continue looking for it
                if nums[middle] == nums[middle - 1]:
                    left = middle + 1
                else:
                    right = middle

        return nums[left]