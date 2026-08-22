class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = defaultdict(list)
        for u, v, price in flights:
            adj[u].append((v, price))

        min_cost = [float('inf')] * n
        min_cost[src] = 0

        queue = deque([(src, 0)])
        stops = 0

        while queue and stops <= k:
            level_size = len(queue)

            for _ in range(level_size):
                curr_node, curr_cost = queue.popleft()

                for neighbor, price in adj[curr_node]:
                    new_cost = curr_cost + price
                    if new_cost < min_cost[neighbor]:
                        min_cost[neighbor] = new_cost
                        queue.append((neighbor, new_cost))

            stops += 1

        return int(min_cost[dst]) if min_cost[dst] != float('inf') else -1