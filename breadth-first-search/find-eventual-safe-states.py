class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        in_degree = defaultdict(int)
        adj = defaultdict(list)

        for i, next_edges in enumerate(graph):
            for edge in next_edges:
                adj[edge].append(i)
                in_degree[i] += 1
        
        queue = deque()
        for i in range(len(graph)):
            if in_degree[i] == 0:  
                queue.append(i)
        
        ans = []
        while queue:
            curr = queue.popleft()
            heapq.heappush(ans, curr)

            for neighbor in adj[curr]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        return ans
