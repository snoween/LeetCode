class Solution:
    def minCostConnectPoints(self, points: list[list[int]]) -> int:
        visited = set()
        n = len(points)

        cost = 0
        heap = [(0, 0)]

        while len(visited) < n:
            curr_cost, curr_node = heapq.heappop(heap)

            if curr_node in visited:
                continue
            
            visited.add(curr_node)

            cost += curr_cost

            x1, y1 = points[curr_node]
            for v in range(n):
                if v not in visited:
                    x2, y2 = points[v]
                    dst = abs(x1 - x2) + abs(y1 - y2)
                    heapq.heappush(heap, (dst, v))
        
        return cost