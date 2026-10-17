class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        n = len(mat)
        mat_copy = mat.copy()

        # Rotate max 3 times to check
        for _ in range(4):
            mat_T = [[0]*n for _ in range(n)]

            # Get transpose matrix
            for i in range(n):
                for j in range(n):
                    mat_T[i][j] = mat_copy[j][i]

            # Reverse each row in transpose matrix
            for row in mat_T:
                row.reverse()

            if mat_T == target:
                return True
            
            mat_copy = mat_T
        
        return False