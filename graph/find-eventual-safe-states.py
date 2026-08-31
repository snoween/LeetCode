class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        in_degree = defaultdict(int)
        
        # build graph and in_degree
        for i, next_edges in enumerate(graph):
            for edge in next_edges:
                adj[edge].append(i)
                in_degree[i] += 1
        
        # build queue with starting points
        queue = deque()
        for i in range(len(graph)):
            if in_degree[i] == 0:  
                queue.append(i)
        
        # loop through queue and check neighbors of current node
        ans = []
        while queue:
            curr = queue.popleft()
            ans.append(curr)

            for neighbor in adj[curr]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        return sorted(ans)
