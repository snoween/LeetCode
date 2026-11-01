class Solution:
    def maxProbability(self, n: int, edges: list[list[int]], succProb: list[float], start_node: int, end_node: int) -> float:
        """
        Solution: Dji, max heap
        """
        # build graph
        graph = defaultdict(list)
        for (u, v), w in zip(edges, succProb):
            graph[u].append((v, w))
            graph[v].append((u, w))
        
        # build dist
        dist = {i: 0.0 for i in range(n)}
        dist[start_node] = -1.0

        # build count
        pop_count = {i: 0 for i in range(n)}

        # build max heap
        heap = [(-1.0, start_node)]

        while heap:
            curr_prob, curr_node = heapq.heappop(heap)
            # check if curr_node is end node -> return because of max heap -> max prob
            if curr_node == end_node:
                return -curr_prob

            # check if negative cycle
            pop_count[curr_node] += 1
            if pop_count[curr_node] >= n:
                return 0
            
            # avoid old state
            if curr_prob < dist[curr_node]:
                continue

            # update new dist if it is smaller
            for v, w in graph[curr_node]:
                new_prob = dist[curr_node] * w
                if new_prob < dist[v]:
                    dist[v] = new_prob
                    heapq.heappush(heap, (new_prob, v))
        
        return dist[end_node]