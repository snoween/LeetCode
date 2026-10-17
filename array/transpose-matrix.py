class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        org_row = len(matrix)
        org_col = len(matrix[0])
        transpose_mat = [[0] * org_row for _ in range(org_col)]

        for i in range(org_row):
            for j in range(org_col):
                transpose_mat[j][i] = matrix[i][j]
        
        return transpose_mat