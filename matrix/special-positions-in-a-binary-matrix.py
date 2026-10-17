class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        sum_row = [0] * m
        sum_col = [0] * n

        # Check if element is 1
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1:
                    sum_row[i] += 1
                    sum_col[j] += 1

        # Check if ele in sum_row = 1, then check if all cols in that row has only one num 1
        count = 0
        for i in range(m):
            if sum_row[i] == 1:
                for j in range(n):
                    if mat[i][j] == 1 and sum_col[j] == 1:
                        count += 1
        
        return count