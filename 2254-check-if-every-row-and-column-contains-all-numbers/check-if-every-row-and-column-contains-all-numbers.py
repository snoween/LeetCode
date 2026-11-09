class Solution:
    def checkValid(self, matrix: list[list[int]]) -> bool:
        n = len(matrix)
        for row in matrix:
            if len(set(row)) != n:
                return False
        
        for i in range(n):
            set_col = set()
            for j in range(n):
                set_col.add(matrix[j][i])
            if len(set_col) != n:
                return False
                
        return True