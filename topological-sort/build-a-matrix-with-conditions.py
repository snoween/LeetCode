class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        """
        - Idea: colConditions: from left to right
        - rowConditions: from top to bottom
        """
        def get_graph(conditions: List[List(int)]):
            adj = defaultdict(list)
            in_degree = defaultdict(int)

            for node, next_node in conditions:
                adj[node].append(next_node)
                in_degree[next_node] += 1

            queue = deque()
            for i in range(1, k + 1):
                if in_degree[i] == 0:
                    queue.append(i)
            
            nodes = []
            while queue:
                curr = queue.popleft()
                nodes.append(curr)

                for neighbor in adj[curr]:
                    in_degree[neighbor] -= 1
                    if in_degree[neighbor] == 0:
                        queue.append(neighbor)

            return nodes

        nodes_row = []
        nodes_col = []
        nodes_row = get_graph(rowConditions)
        nodes_col = get_graph(colConditions)

        # check if the list of nodes in row/col has cycle or not
        if len(nodes_row) != k or len(nodes_col) != k:
            return []
        
        # get the coordinates for each node
        coor = defaultdict(list)
        for i in range(k):
            coor[nodes_row[i]].append(i)
        for j in range(k):
            coor[nodes_col[j]].append(j)
        
        # Update matrix k x k
        matrix = [[0] * k for _ in range(k)]
        for node, val in coor.items():
            x, y = val
            matrix[x][y] = node
        
        return matrix
