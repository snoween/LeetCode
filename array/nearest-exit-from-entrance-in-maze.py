class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        """
        - Algorithm: BFS, no layers
        - Time comp: O(N)
        - Space comp: O(N)
        """

        m, n = len(maze), len(maze[0])
        DIRS = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        # Set init stack and append entrance
        queue = deque()
        queue.append([entrance[0], entrance[1]])
        # Use set for storing visited coor
        visited = set()
        visited.add(tuple(entrance))

        #set init step = 0
        steps = 0

        while queue:
            x, y = queue.popleft()
            # increase step by 1 for moving 1 step forward
            steps += 1

            # check neighbors
            for coor in DIRS:
                newX = x + coor[0]
                newY = y + coor[1]

                if 0 <= newX < m and 0 <= newY < n and maze[newX][newY] == '.':
                    if (newX, newY) not in visited:
                        queue.append([newX, newY])
                        visited.add((newX, newY))
                    
                    if (newX == 0 or newX == m - 1) or (newY == 0 or newY == n - 1):
                        if (newX, newY) != tuple(entrance):
                            return steps

        # if no paths -> return -1
        return -1
