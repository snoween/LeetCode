class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        """
        - Time comp: O(N x N)
        - Space comp: O(1) - in place
        - Algorithm: only swap numbers not on x = y, which means with each
        row, we have to loop col from row + 1 -> n
        - Use .reverse() to modify in place
        """

        n = len(matrix)
        
        for r in range(n):
            for c in range(r + 1, n):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
            
            matrix[r].reverse()