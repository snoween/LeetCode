class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            middle = left + (right - left) // 2
            print(middle)
            if nums[middle] == target:
                return middle

            if nums[middle] <= nums[right]:
                if nums[middle] < target <= nums[right]:
                    left = middle + 1
                else:
                    right = middle - 1
            else:
                if nums[left] <= target < nums[middle]:
                    right = middle - 1
                else:
                    left = middle + 1

        return -1
