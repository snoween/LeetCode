class Solution:
    def minimumEffortPath(self, heights: list[list[int]]) -> int:
        """
        Solution: DJI - weights > 0
        - Grid is a graph -> no need to build graph
        - weight = abs(curr_cell, adj_node)
        - use min heap with init value = [0, 0 ,0] - [dist, r, c]
        - build dist grid with inf val
        """
        rows, cols = len(heights), len(heights[0])
        DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        # build grid dist
        dist = [[float('inf')] * cols for _ in range(rows)]
        dist[0][0] = 0

        # build heap - [dist, r, c]
        heap = [(0, 0, 0)]

        while heap:
            curr_dist, r, c = heapq.heappop(heap)

            # if reach the bottom right cell -> return result
            if r == rows - 1 and c == cols - 1:
                return curr_dist

            if curr_dist > dist[r][c]:
                continue
            
            for x, y in DIRS:
                newX, newY = x + r, y + c

                if not (0 <= newX < rows and 0 <= newY < cols):
                    continue
                
                step_effort = abs(heights[newX][newY] - heights[r][c])
                new_effort = max(step_effort, curr_dist)

                if new_effort < dist[newX][newY]:
                    dist[newX][newY] = new_effort
                    heapq.heappush(heap, (new_effort, newX, newY))