class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None

class Solution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        # build trie
        root = TrieNode()
        for word in words:
            node = root
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.word = word

        DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        row, col = len(board), len(board[0])
        result = []

        def backtrack(x, y, node):
            char = board[x][y]
            curr_node = node.children[char]
            # if the current node is the end of a word -> append to result
            if curr_node.word is not None:
                result.append(curr_node.word)
                curr_node.word = None    # to avoid duplicate (eg app, apple)
            
            # mark visited
            board[x][y] = '#'

            for dx, dy in DIRS:
                nx = x + dx
                ny = y + dy
                if not 0 <= nx < row or not 0 <= ny < col:
                    continue

                if board[nx][ny] in curr_node.children:
                    backtrack(nx, ny, curr_node) 
            # undo
            board[x][y] = char


        for i in range(row):
            for j in range(col):
                if board[i][j] in root.children:
                    backtrack(i, j, root)
        
        return result