class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        edges = len(connections)

        parent = {i: i for i in range(n)}
        size = {i: 1 for i in range(n)}

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            parentX, parentY = find(x), find(y)

            if parentX == parentY:
                return False
            
            if size[parentX] < size[parentY]:
                parent[parentX] = parentY
                size[parentY] += size[parentX]
            else:
                parent[parentY] = parentX
                size[parentX] += size[parentY]
            
            return True
        
        for u, v in connections:
            if union(u, v):
                edges -= 1
        
        connected_components = len(set(parent.values()))
        if connected_components - 1 == edges:
            return edges
        
        return -1