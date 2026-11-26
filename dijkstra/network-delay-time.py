class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # build graph
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((w, v))
        
        # build dist 
        dist = {i: float('inf') for i in range(1, n + 1)}
        dist[k] = 0

        # min heap
        heap = [(0, k)]

        while heap:
            curr_dist, curr_node = heapq.heappop(heap)

            if curr_dist > dist[curr_node]:
                continue
            
            for w, v in graph[curr_node]:
                new_dist = curr_dist + w
                if new_dist < dist[v]:
                    dist[v] = new_dist
                    heapq.heappush(heap, (new_dist, v))
        
        min_time = max(dist.values())
        if min_time == float('inf'):
            return -1
        
        return min_time