class Solution:
    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
        """
        Solution: BFS
        - Time comp: O(V x E)
        - weights > 0
        intit: [0, 0]
        -> loop neighbor queue = [100, 1]
        from 1 -> check neighbors 2, 3 -> update dist[2] = 200, dist[3] = 700, stop = 1, always update dist[v] when find shorter path -> return dist[dst] if != inf
        """
        # build graph
        graph = defaultdict(list)
        for u, v, w in flights:
            graph[u].append((w, v))
        
        # build dist
        cost = {i: float('inf') for i in range(n)}
        cost[src] = 0

        # build queue
        queue = deque([(0, src)])

        stops = 0
        while queue and stops <= k:
            for _ in range(len(queue)):
                curr_cost, curr_node = queue.popleft()

                for w, v in graph[curr_node]:
                    new_cost = curr_cost + w
                    if new_cost < cost[v]:
                        cost[v] = new_cost
                        queue.append((new_cost, v))
            # update stops count
            stops += 1
        
        # check if valid cost
        if cost[dst] == float('inf'):
            return -1
        
        return cost[dst]