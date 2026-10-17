class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)

        # build graph
        for u, v, w in flights:
            graph[u].append((v, w))
        
        # distance array
        cost = {i: float(inf) for i in range(n)}
        cost[src] = 0

        # queue
        queue = deque([(src, 0)])
        stop = 0

        while queue and stop <= k:
            length = len(queue)

            for _ in range(length):
                node, curr_cost = queue.popleft()

                for neighbor, weight in graph[node]:
                    new_cost = curr_cost + weight
                    if new_cost < cost[neighbor]:
                        cost[neighbor] = new_cost
                        queue.append((neighbor, new_cost))

            stop += 1
        
        if cost[dst] == float(inf):
            return -1

        return cost[dst]