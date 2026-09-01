class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        """
        - Idea: colConditions: from left to right
        - rowConditions: from top to bottom
        """
        adj_row = []
        adj_col = []

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
            
            order = []
            while queue:
                curr = queue.popleft()
                order.append(curr)

                for neighbor in adj[curr]:
                    in_degree[neighbor] -= 1
                    if in_degree[neighbor] == 0:
                        queue.append(neighbor)

            return order

        adj_row = get_graph(rowConditions)
        adj_col = get_graph(colConditions)

        if len(adj_row) != k or len(adj_col) != k:
            return []
        
        coor = defaultdict(list)

        print(adj_row, adj_col)
        for i in range(k):
            coor[adj_row[i]].append(i)
        for j in range(k):
            coor[adj_col[j]].append(j)
        
        matrix = [[0] * k for _ in range(k)]
        for node, val in coor.items():
            matrix[val[0]][val[1]] = node
        
        return matrix
