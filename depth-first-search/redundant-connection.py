class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = {i: i for i in range(1, n+ 1)}
        size = {i: 1 for i in range(1, n + 1)}
        
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
        
        for u, v in edges:
            
            if not union(u, v):
                return [u, v]