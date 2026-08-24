class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        is_col = False      # mark for the first col

        # mark 0 elements in matrix, only in first row/col element
        # matrix will looks like: [0 1 2], [1 2 0] -> [0 1 0], [0 2 0]
        for r in range(m):
            if matrix[r][0] == 0:   # just need to check the first col has any 0
                is_col = True
            for c in range(1, n):   
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    matrix[r][0] = 0


        # loop through matrix -> change all elements in those rows, cols to 0
        # start from row = 1, col = 1
        for r in range(1, m):
            for c in range(1, n):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0

        # work on the first row and first col
        if matrix[0][0] == 0:
            for c in range(n):
                matrix[0][c] = 0

        if is_col:    
            for r in range(m):
                matrix[r][0] = 0