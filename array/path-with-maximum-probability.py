class Solution:
    def maxProbability(self, n: int, edges: list[list[int]], succProb: list[float], start_node: int, end_node: int) -> float:
        """
        Solution: Dji, max heap
        """
        graph = defaultdict(list)
        for (u, v), w in zip(edges, succProb):
            graph[u].append((w, v))
            graph[v].append((w, u))
        
        dist = {i: 0.0 for i in range(n)}
        dist[start_node] = -1.0

        visited = set()
        heap = [(-1.0, start_node)]

        while heap:
            curr_prob, curr_node = heapq.heappop(heap)

            if curr_node == end_node:
                return -curr_prob
            
            if curr_prob > dist[curr_node]:
                continue
            
            if curr_node in visited:
                return 0
            
            visited.add(curr_node)

            for w, v in graph[curr_node]:
                new_prob = curr_prob * w
                if new_prob < dist[v]:
                    dist[v] = new_prob
                    heapq.heappush(heap, (new_prob, v))
        
        return dist[end_node]