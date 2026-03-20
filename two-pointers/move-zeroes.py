class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        first_0_idx = -1

        for i in range(len(nums)):
            if nums[i] == 0:
                first_0_idx = i
                break

        if first_0_idx == -1:
            return nums 
        
        for j in range(first_0_idx + 1, len(nums)):
            if nums[j] != 0:
                nums[first_0_idx], nums[j] = nums[j], nums[first_0_idx]
                first_0_idx += 1