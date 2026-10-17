class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        result = []
        # set up list of bool for col, ascending/descending diagonals
        col = [True] * n
        asc_diag = [True] * (n * 2 - 1)     # total num of diagonals
        des_diag = [True] * (n * 2 - 1)

        def backtrack(queens):
            curr_row = len(queens)

            if curr_row == n:
                board = ["." * c + "Q" + "." * (n - c - 1) for c in queens]
                result.append(board)
                return 

            for curr_col in range(n):
                # make choices
                if not col[curr_col]:
                    continue
                if not asc_diag[curr_col + curr_row]:
                    continue
                if not des_diag[curr_col - curr_row]:
                    continue
                    
                col[curr_col] = False
                asc_diag[curr_col + curr_row] = False
                des_diag[curr_col - curr_row] = False

                # backtrack
                queens.append(curr_col)
                backtrack(queens)

                # undo
                col[curr_col] = True
                asc_diag[curr_col + curr_row] = True
                des_diag[curr_col - curr_row] = True
                queens.pop()

        backtrack([])
        return result