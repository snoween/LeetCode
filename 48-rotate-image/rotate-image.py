class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)

        # loop col starts from 1 to avoid swap 1 element twice
        for r in range(n):
            for c in range(r + 1, n):
                temp = matrix[r][c]
                matrix[r][c] = matrix[c][r]
                matrix[c][r] = temp
        
        # reverse row 
        for r in range(n):
            matrix[r] = matrix[r][::-1]