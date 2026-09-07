class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        parent = {}
        size = {}
        
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
        
        # build DSU
        email_to_name = {}
        for acc in accounts:
            name = acc[0]
            for i in range(1, len(acc)):
                email = acc[i]
                if email not in parent:
                    parent[email] = email
                    size[email] = 1
                
                email_to_name[email] = name
                union(acc[1], email)    # merge to 1 tree
        
        # build dict of components
        components = defaultdict(list)
        for email in parent:
            root = find(email)
            components[root].append(email)
        
        # get result
        result = []
        for root, emails in components.items():
            name = email_to_name[root]
            sorted_emails = sorted(emails)
            result.append([name] + sorted_emails)       # list name + list sorted mails
        
        return result
                