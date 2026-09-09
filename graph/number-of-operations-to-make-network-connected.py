class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        connected_components = n
        edges = len(list(connections))

        # if connected components - 1 > edges -> not enough cables to connect all machines
        if connected_components - 1 > edges:
            return -1
        
        # build parent, size
        parent = {i: i for i in range(n)}
        size = {i: 1 for i in range(n)}

        # func to find parent, if same tree -> change to same parent
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        # func to merge trees
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

        # build connection 
        for x, y in connections:
            if union(x, y):
                connected_components -= 1
        
        return connected_components - 1     # remaining edges to connect all of them