class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row, col = len(matrix), len(matrix[0])

        l = 0
        r = row - 1
        ans = 0
        # tim kiem tren hang nao
        while l <= r:
            m = l + (r - l) // 2
            if matrix[m][0] <= target:
                ans = m
                l = m + 1
            else:
                r = m - 1

        # tim kiem tren hang ans
        l = 0
        r = col-1

        while l <= r:
            m = l + (r - l) // 2
            if matrix[ans][m] == target:
                return True
            if matrix[ans][m] > target:
                r = m - 1
            else:
                l = m + 1
        
        return False