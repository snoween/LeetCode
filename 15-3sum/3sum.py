class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        """
        Solution: 2 pointers
        - Sort the array
        - To avoid duplicate:
            - compare the current target vs prev target
            - compare the next left num vs curr left num
            - compare the next right num vs curr right num
        """

        nums.sort()
        result = []
        for i, num in enumerate(nums):
            if i > 0 and num == nums[i - 1]:
                continue

            left, right = i + 1, len(nums) - 1
            while left < right:
                if nums[left] + nums[right] + num > 0:
                    right -= 1
                elif nums[left] + nums[right] + num < 0:
                    left += 1
                else:
                    result.append([num, nums[left], nums[right]])
                    left += 1
                    right -= 1

                    # check if next left num is equal to prev left num
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    
                    # check right num 
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

        return result