class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        """
        - Solution: Diameter tree. The tree can have maximum 2 central points
        - queue at beginning stores nodes with in_degree = 0 (leaves)
        - BFS layer by layer
        - Stop the while loop when n <= 2 -> The nodes in queue will be valid roots
        """

        # Edge case: 1 node 
        if n == 1:
            return [0]
        
        # Build adj and in_degree
        adj = defaultdict(list)
        in_degree = defaultdict(int)

        for u, v in edges:
            adj[u].append(v)
            in_degree[v] += 1

            adj[v].append(u)
            in_degree[u] += 1
        
        # Put nodes with in_degree = 1 into queue
        queue = deque()
        for node, val in in_degree.items():
            if val == 1:
                queue.append(node)

        # BFS layer by layer, stop while loop when n <= 2, remaining nodes are central points aka valid roots
        while n > 2:
            length = len(queue)

            for _ in range(length):
                curr = queue.popleft()
                n -= 1
                for neighbor in adj[curr]:
                    in_degree[neighbor] -= 1
                    if in_degree[neighbor] == 1:
                        queue.append(neighbor)
        
        return list(queue)