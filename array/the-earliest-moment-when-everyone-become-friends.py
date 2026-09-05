class Solution:
    def earliestAcq(self, logs, n):
        parent = {i: i for i in range(n)}
        size = {i : 1 for i in range(n)}

        connected = n

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
        
        logs.sort()

        for t, u, v in logs:
            if union(u, v):
                connected -= 1
                if connected == 1:
                    return t
        
        return -1