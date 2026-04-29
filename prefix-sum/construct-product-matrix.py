class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        prod = 1
        mod = 12345
        output = [[1]*n for i in range(m)]
        
        for i in range(m):
            for j in range(n):
                prod *= grid[i][j]
        
        for i in range(m):
            for j in range(n):
                element = prod // grid[i][j]
                output[i][j] = element if element % mod != 0 else 0

        return output