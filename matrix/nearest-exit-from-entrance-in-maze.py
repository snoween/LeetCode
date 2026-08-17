class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        """
        Algorithm: BFS - level transversal
        Time comp: O(M x N)
        Space comp: O(M x N)
        """
        m, n = len(maze), len(maze[0])
        # neighbors
        DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        # queue to store boxes which need to be processed
        queue = deque()
        queue.append((entrance[0], entrance[1]))

        # visited to store visited box
        visited = set()
        visited.add((entrance[0], entrance[1]))

        # set init step = 0
        steps = 0

        while queue:
            len_queue = len(queue)
            # update steps
            steps += 1

            # process all boxes in that level to make sure no confusion about increasing steps
            for _ in range(len_queue):
                # get current coordinates
                x, y = queue.popleft()
                # loop to get all neighbors values
                for neighbor in DIRS:
                    newX = x + neighbor[0]
                    newY = y + neighbor[1]

                    # check if new coors are valid, and value of that box is valid to move forward
                    if 0 <= newX < m and 0 <= newY < n and maze[newX][newY] == '.':
                        # check if that box is never met before -> append to queue and visited
                        if (newX, newY) not in visited:
                            queue.append((newX, newY))
                            visited.add((newX, newY))
                        
                        # if the exit box != entrance -> return num steps
                        if newX == 0 or newX == m - 1 or newY == 0 or newY == n - 1:
                            if (newX, newY) != tuple(entrance):
                                return steps

        # if no valid paths -> return -1
        return -1