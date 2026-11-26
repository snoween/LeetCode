class Solution:
    def countPaths(self, n: int, roads: list[list[int]]) -> int:
        """
        Solution: DJI
        - Shortest time -> min heap
        - if dist[n - 1] = min time -> count + 1
        """
        mod = 10 ** 9 + 7
        # build graph
        graph = defaultdict(list)
        for u, v, w in roads:
            graph[u].append((v, w))
            graph[v].append((u, w))
        
        # build dist
        dist = {i: float('inf') for i in range(n)}
        dist[0] = 0
        
        # build number of paths
        path = {i: 0 for i in range(n)}
        path[0] = 1     # have 1 way to go to the starting point

        # build min heap, init val = (dist starting node, node)
        heap = [(0, 0)]

        # loop through heap
        while heap:
            curr_dist, curr_node = heapq.heappop(heap)
            
            # check if curr_dist > dist[curr_node] -> continue
            if curr_dist > dist[curr_node]:
                continue

            # update distance to adj nodes
            for v, w in graph[curr_node]:
                new_dist = curr_dist + w
                if new_dist < dist[v]:
                    dist[v] = new_dist
                    path[v] = path[curr_node]       # path[v] = take all paths from u
                    heapq.heappush(heap, (new_dist, v))
                elif new_dist == dist[v]:
                    path[v] = (path[v] + path[curr_node]) % mod

        return path[n - 1]