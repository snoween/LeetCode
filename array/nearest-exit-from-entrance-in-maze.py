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
        stack = [tuple(entrance)]
        # Use set for storing visited coor
        visited = set()
        visited.add(tuple(entrance))

        #set init step = 0
        steps = 0

        while stack:
            x, y = stack.pop()
            # increase step by 1 for moving 1 step forward
            steps += 1

            # check neighbors
            for coor in DIRS:
                newX = x + coor[0]
                newY = y + coor[1]

                if 0 <= newX < m and 0 <= newY < n and maze[newX][newY] == '.':
                    if (newX, newY) not in visited:
                        stack.append((newX, newY))
                        visited.add((newX, newY))
                    
                    if (newX == 0 or newX == m - 1) or (newY == 0 or newY == n - 1):
                        if (newX, newY) != tuple(entrance):
                            return steps

        # if no paths -> return -1
        return -1
