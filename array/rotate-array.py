class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def rotate(nums, left, right):
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
                
        n = len(nums)
        k = k % n
        rotate(nums, 0, n - 1)
        rotate(nums, 0, k - 1)
        rotate(nums, k, n - 1)
