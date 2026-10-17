class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        sum_diag = 0
        n = len(mat)

        for i in range(n):
            sum_diag += mat[i][i] 
            if i != (n-i-1):    # To avoid mat[i][i]
                sum_diag += mat[i][n-i-1] 
            
        return sum_diag