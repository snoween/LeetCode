class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # build graph
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
        
        # build distance array
        dist = {i : float(inf) for i in range(1, n + 1)}
        dist[k] = 0

        # build init heap with starting point k
        heap = [(0, k)]
        max_time = 0
        while heap:
            curr_dist, curr_node = heapq.heappop(heap)

            # if the current distance > last distance -> continue
            if curr_dist > dist[curr_node]:
                continue
            
            # loop through its adjacent nodes
            for v, w in graph[curr_node]:
                if dist[curr_node] + w < dist[v]:
                    dist[v] = dist[curr_node] + w
                    heapq.heappush(heap, (dist[v], v))
        
        max_time = max(dist.values())
        return max_time if max_time != inf else -1