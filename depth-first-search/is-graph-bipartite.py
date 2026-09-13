class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        """
        Method: Union Find
        """
        n = len(graph)
        parent = {i: i for i in range(n)}

        def find(x): 
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            parentX, parentY = find(x), find(y)
            if parentX != parentY:
                parent[parentX] = parentY
        
        for u in range(n):
            for v in graph[u]:
                if find(u) == find(v):
                    return False

                union(graph[u][0], v)   # Merge all nodes in graph[u]
        
        return True

