class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        """
        Solution: binary search
        - Take left = 0, right = rows * cols - 1
        - Calculate middle
        - Reverse middle to: row = middle // cols, col = middle % cols
        - Compare matrix[row][col] vs target
        """
        rows, cols = len(matrix), len(matrix[0])
        left = 0
        right = rows * cols - 1

        while left <= right:
            middle = left + (right - left) // 2

            row = middle // cols
            col = middle % cols
    
            if matrix[row][col] > target:
                right = middle - 1
            elif matrix[row][col] < target:
                left = middle + 1
            else:
                return True

        return False