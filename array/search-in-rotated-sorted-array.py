class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        Idea: Binary search
        - Find left rotated part
        - If num middle < num right -> check if target in right side or not
        - else: check if target in left side or not
        - Use binary search to check each part
        
        """
        left, right = 0, len(nums) - 1

        while left <= right:
            middle = left + (right - left) // 2

            # check if num middle = target
            if nums[middle] == target:
                return middle
            
            # target in half right
            if nums[middle] <= nums[right]:
                if nums[middle] < target <= nums[right]:
                    left = middle + 1
                else:
                    right = middle - 1
            # if target in half left
            else:   
                if nums[left] <= target < nums[middle]:
                    right = middle - 1
                else:
                    left = middle + 1
        
        return -1