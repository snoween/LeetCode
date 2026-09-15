class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        """
        Solution: Union Find
        merge all emails in 1 list 
        """
        # 1. Build union find with parent and size
        parent = defaultdict(str)
        size = {}

        for list_mails in accounts:
            for i in range(1, len(list_mails)):
                parent[list_mails[i]] = list_mails[i]
                if list_mails[i] not in size:
                    size[list_mails[i]] = 1
        
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
        
        # Loop through list accounts to merge emails with same user
        main_mail_user = defaultdict(list)
        for list_mails in accounts:
            user = list_mails[0]
            root = list_mails[1]
            if root not in main_mail_user:
                main_mail_user[root].append(user)

            for i in range(1, len(list_mails)):
                union(root, list_mails[i])
        
        # Match user with their main account
        user_mail = defaultdict(list)
        for email in parent:
            root = find(email)
            user_mail[root].append(email)
        
        # get ans
        result = []
        for main_mail, sub_mail in user_mail.items():
            name = main_mail_user[main_mail]
            all_emails = sorted(user_mail[main_mail])
            result.append(name + all_emails) 
        
        return result
        
