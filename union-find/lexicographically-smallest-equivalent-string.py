class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        n = len(s1)
        parent = {}
        size = {}
        
        for i in range(n):
            if s1[i] not in parent: 
                parent[s1[i]] = s1[i]
                size[s1[i]] = 1
            
            if s2[i] not in parent:
                parent[s2[i]] = s2[i]
                size[s2[i]] = 1
        
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
        
        # group characters
        for i in range(n):
            union(s1[i], s2[i])
        
        # group all elements with same root
        lex_order = defaultdict(list)
        for char, root in parent.items():
            lex_order[root].append(char)
        
        ans = []
        for ele in baseStr:
            if ele not in parent:
                ans.append(ele)
                continue

            parentEle = find(ele)
            ans.append(min(lex_order[parentEle]))
        
        return ''.join(ans)
        
       