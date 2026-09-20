class Solution:
    def predictTheWinner(self, nums: list[int]) -> bool:
        """
        Solution: recursion
        Get the maximum diff scores when player 1 takes 
        left/right. If diff > 0 -> player 1 wins
        """
        left, right = 0, len(nums) - 1

        def max_diff(left, right):
            # stop when array has 1 element
            if left == right:
                return nums[left]
            
            take_left = nums[left] - max_diff(left + 1, right)
            #print(take_left)
            take_right = nums[right] - max_diff(left, right - 1)
            #print(take_right)
            return max(take_left, take_right)
        
        #print(max_diff(left, right))
        return max_diff(left, right) > 0