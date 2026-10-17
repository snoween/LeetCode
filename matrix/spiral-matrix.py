class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        """
        Solution: 
        - Append top row -> right col -> bottom row -> left col
        - Time comp: O(M x N)
        - Space comp: O(M x N) for result, O(1) for top, bottom, left, right
        """
        rows, cols = len(matrix), len(matrix[0])

        # Get 4 starting points
        top = 0
        bottom = rows - 1
        left = 0
        right = cols - 1

        result = []
        while top <= bottom and left <= right:
            # Top row
            for i in range(left, right + 1):
                result.append(matrix[top][i])
            top += 1

            # Right col
            for j in range(top, bottom + 1):
                result.append(matrix[j][right])
            right -= 1

            # Bottom row
            if top <= bottom:
                for k in range(right, left - 1, -1):
                    result.append(matrix[bottom][k])
                bottom -= 1
            
            # Left col
            if left <= right:
                for v in range(bottom, top - 1, -1):
                    result.append(matrix[v][left])
                left += 1
        
        return result
