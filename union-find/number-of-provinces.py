class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        
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
        
        connected_components = n
        for r in range(n):
            for c in range(r + 1, n):    #only check upper half triangle of the matrix
                if isConnected[r][c] == 1:
                    if union(r, c):
                        connected_components -= 1
        
        return connected_components