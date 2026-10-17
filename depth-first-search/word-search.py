class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        rows, cols = len(board), len(board[0])
        
        def backtrack(x, y, index):
            if index == len(word):
                return True
            
            if not 0 <= x < rows or not 0 <= y < cols or board[x][y] != word[index]:
                return False
            
            curr_char = board[x][y]
            board[x][y] = '#'
            
            for dx, dy in DIRS:
                nx = x + dx
                ny = y + dy
                
                if backtrack(nx, ny, index + 1):
                    return True
            
            board[x][y] = curr_char
            return False
        
        # loop through grid, only backtrack if meet the first char in word
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0] and backtrack(i, j, 0):
                    return True
        
        return False