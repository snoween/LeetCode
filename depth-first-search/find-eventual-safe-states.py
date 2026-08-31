class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        terminal_node = set()
        for i, edge in enumerate(graph):
            if not edge:
                terminal_node.add(i)
        
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
            ans.append(curr)

            for neighbor in adj[curr]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        return sorted(ans)
