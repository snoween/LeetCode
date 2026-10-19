class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        """
        Solution: sliding window with k elements
        - the init window will be the whole array
        - shrink the window until it reaches size k
        - calculate the value of left and right pointers 
        -> move the farther pointer
        """

        left, right = 0, len(arr) - 1

        # loop until the size of the window is equal to k
        while right - left + 1 > k:
            # left pointer is closer than right pointer -> move right
            if abs(arr[left] - x) <= abs(arr[right] - x):
                right -= 1
            else:   # else move left pointer
                left += 1
        
        return arr[left:right + 1]