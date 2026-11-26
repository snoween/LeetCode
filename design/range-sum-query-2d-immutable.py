class NumMatrix:

    def __init__(self, matrix: list[list[int]]):
        m, n = len(matrix), len(matrix[0])
        self.prefix = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                self.prefix[i][j] = (
                matrix[i - 1][j - 1] 
                + self.prefix[i - 1][j]    # + left
                + self.prefix[i][j - 1]    # + top
                - self.prefix[i - 1][j - 1]   # - top left
                )

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # convert 0-based index -> 1-based index
        r1, c1 = row1 + 1, col1 + 1
        r2, c2 = row2 + 1, col2 + 1

        return (self.prefix[r2][c2]
                - self.prefix[r1 - 1][c2]
                - self.prefix[r2][c1 - 1]
                + self.prefix[r1 - 1][c1 - 1]
                )


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)