class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        DIRS = [(0, 0), (0, 1), (0, 2),
                (1, 0), (1, 1), (1, 2),
                (2, 0), (2, 1), (2, 2)]
        n = len(board)

        # Check if num appears in row again
        for row in range(n):
            set_row = set()
            set_col = set()
            for col in range(n):
                if board[row][col].isdigit() and board[row][col] in set_row:
                    return False
                set_row.add(board[row][col])
                
                if board[col][row].isdigit() and board[col][row] in set_col:
                    return False
                set_col.add(board[col][row])
        
                if row % 3 == 0 and col % 3 == 0:
                    set_mat = set()
                    for ni, nj in DIRS:
                        ni = row + ni
                        nj = col + nj
                        if board[ni][nj].isdigit() and board[ni][nj] in set_mat:
                            return False

                        set_mat.add(board[ni][nj])
        
        return True