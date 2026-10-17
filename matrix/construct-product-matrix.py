class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        mod = 12345

        output = [[1]* n for i in range(m)]
        prefix = defaultdict(lambda: 1)
        suffix = defaultdict(lambda: 1)

        # Get prefix of grid[i][j], except itself
        k = 1
        for i in range(m):
            for j in range(n):
                prefix[k] = (prefix[k-1] * grid[i][j]) % mod
                k += 1
        
        # Get prefix of grid[i][j], except itself
        v = (m*n) - 2
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                suffix[v] = (suffix[v+1] * grid[i][j]) % mod
                v -= 1

        # Get output
        u = 0
        for i in range(m):
            for j in range(n):
                output[i][j] = (prefix[u] * suffix[u]) % mod
                u += 1
        
        return output

