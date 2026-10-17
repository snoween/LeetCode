class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        DIRS = [(0, 0), (0, 1), (0, 2),
                (1, 0), (1, 1), (1, 2),
                (2, 0), (2, 1), (2, 2)]
        
        n = 9
        for i in range(n):
            set_row = set()
            set_col = set()
            for j in range(n):
                if board[i][j].isdigit() and board[i][j] in set_row:
                    return False
                if  board[j][i].isdigit() and board[j][i] in set_col:
                    return False
                set_row.add(board[i][j])
                set_col.add(board[j][i])

                if i % 3 == 0 and j % 3 == 0:
                    set_mat = set()
                    for x, y in DIRS:
                        newX = i + x
                        newY = j + y

                        if board[newX][newY].isdigit() and board[newX][newY] in set_mat:
                            return False
                        set_mat.add(board[newX][newY])
        
        return True