class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        row, col = len(maze), len(maze[0])
        DIRS = [(0, 1), (-1, 0), (0, -1), (1, 0)]

        # queue to save next step
        queue = deque()
        queue.append(entrance)

        seen_step = set()
        seen_step.add(tuple(entrance))

        layer = 0
        while queue:
            n = len(queue)
            layer += 1
            for _ in range(n):
                curr_position = queue.popleft()
                for coor in DIRS:
                    next_row = curr_position[0] + coor[0]
                    next_col = curr_position[1] + coor[1]

                    if 0 <= next_row < row and 0 <= next_col < col and maze[next_row][next_col] == '.':
                        if tuple([next_row, next_col]) not in seen_step:
                            queue.append([next_row, next_col])
                            seen_step.add(tuple([next_row, next_col]))
                        
                        if (next_row == 0 or next_row == row - 1) or (next_col == 0 or next_col == col - 1):
                            return layer

        return -1