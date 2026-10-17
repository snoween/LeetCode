class Solution:
    def totalNQueens(self, n: int) -> int:
        """
        Solution: backtracking
        - Each row, col, ascending diaganol, descending diaganol only have
        1 queen
        - Use 3 arrays (True val, size n for col, size n * 2 - 1 for diaganol) to label if that position is valid to put a queen
        - Mark that position in those 3 arrays as False when we put a queen
        - Backtrack to explore deeper in next row
        - Undo: when the position is invalid -> change the status of previous
        position in those 3 arrays back to True
        """
        count = 0

        col = [True] * n
        asc_diag = [True] * (n * 2 - 1)
        des_diag = [True] * (n * 2 - 1)

        def backtrack(index):
            nonlocal count, col, asc_diag, des_diag
            # return when we put n queens on board (reach the last row)
            if index == n:
                count += 1
                return
            
            curr_row = index
            # make choices
            for curr_col in range(n):
                # check if col/asc diag/ des diag is valid
                if not col[curr_col]:   
                    continue 
                if not asc_diag[curr_row + curr_col]:
                    continue
                if not des_diag[curr_row - curr_col]:
                    continue
                
                # mark visited
                col[curr_col] = False
                asc_diag[curr_row + curr_col] = False
                des_diag[curr_row - curr_col] = False

                # backtrack
                backtrack(index + 1)

                # undo
                col[curr_col] = True
                asc_diag[curr_row + curr_col] = True
                des_diag[curr_row - curr_col] = True
        
        backtrack(0)
        return count
