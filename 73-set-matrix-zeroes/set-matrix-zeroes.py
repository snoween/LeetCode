class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        # get set of row, col has 0
        set_row = set()
        set_col = set()
        for r in range(m):
            for c in range(n):
                if matrix[r][c] == 0:
                    set_row.add(r)
                    set_col.add(c)

        print(set_row, set_col)
        # loop through the 2 sets -> change all elements in those rows, cols to 0
        for x in range(m):
            if x in set_row:
                for y in range(n):
                    matrix[x][y] = 0

        for y in range(n):
            if y in set_col:
                for x in range(m):
                    matrix[x][y] = 0

                
