

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = {i : i for i in range(n)}
        size = {i : 1 for i in range(n)}
        connected = n
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            parentX, parentY = find(x), find(y)

            if parentX == parentY:
                return
            
            if size[parentX] < size[parentY]:
                parent[parentX] = parentY
                size[parentY] += size[parentX]
            else:
                parent[parentY] = parentX
                size[parentX] += size[parentY]
            
        for u, v in edges:

            if not union(u, v):
                connected -= 1

        return connected