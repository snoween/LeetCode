class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        """
        - Idea: do as normal but for reversed graph
        """
        adj = defaultdict(list)
        in_degree = defaultdict(int)
        safe_node = [False] * len(graph)

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
        while queue:
            curr = queue.popleft()
            safe_node[curr] = True

            for neighbor in adj[curr]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        # get final answer
        ans = []
        for node, state in enumerate(safe_node):
            if state:
                ans.append(node)

        return ans
