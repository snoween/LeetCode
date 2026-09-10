class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        parent = {chr(i): chr(i) for i in range(ord('a'), ord('z') + 1)}
        print(parent)
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            parentX, parentY = find(x), find(y)
            if parentX == parentY: 
                return 
            
            if parentX < parentY:
                parent[parentY] = parentX
            else:
                parent[parentX] = parentY
                
        for c1, c2 in zip(s1, s2):
            union(c1, c2)
        
        return ''.join(find(char) for char in baseStr)
        