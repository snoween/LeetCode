class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        """
        Use only first row/col to check if that row/col has 0
        -> Change the remaining of row/col to 0
        """
        m, n = len(matrix), len(matrix[0])
        first_col_zero = False

        for i in range(m):
            if matrix[i][0] == 0:
                first_col_zero = True
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0    # Mark on the first row which column has 0
                    matrix[i][0] = 0    # Mark on the first col which row has 0
            
        for x in range(1, m):
            for y in range(1, n):
                if matrix[0][y] == 0 or matrix[x][0] == 0:
                    matrix[x][y] = 0
        
        if matrix[0][0] == 0:
            for c in range(n):
                matrix[0][c] = 0

        if first_col_zero:    
            for r in range(m):
                matrix[r][0] = 0
