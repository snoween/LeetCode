class Solution:
    def minimumSwaps(self, nums: list[int]) -> int:
        # 2 pointers, swap only when nums[left] = 0, nums[right] != 0
        left, right = 0, len(nums) - 1
        count = 0

        while left < right:
            # Find the first 0 from the left
            while left < right and nums[left] != 0:
                left += 1

            # Find the first non 0 from the right
            while left < right and nums[right] == 0:
                right -= 1

            # swap left and right numbers
            if left < right:
                nums[left], nums[right] = nums[right], nums[left]
                count += 1
            
        return count