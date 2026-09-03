class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        # build graph
        graph = defaultdict(list)
        # build in_degree of each node
        in_degree = defaultdict(int)

        for u, v in edges:
            graph[u].append(v)
            in_degree[v] += 1
        
        # build dict ancestors with values are set of ancestors of previous node
        ancestors = {i: set() for i in range(n)}

        # append to queue all starting nodes (in_degree[node] = 0)
        queue = deque()
        for i in range(n):
            if in_degree[i] == 0:
                queue.append(i)

        while queue:   
            curr = queue.popleft()      # popleft queue to get curr node

            for neighbor in graph[curr]:
                ancestors[neighbor].add(curr)       # neighbor has ancestor = add curr node
                ancestors[neighbor].update(ancestors[curr])      # update neighbor ancestor = curr node ancestor
                
                in_degree[neighbor] -= 1    # decrease in degree of neighbor by 1
                if in_degree[neighbor] == 0:    # if in degree = 0 -> append to queue
                    queue.append(neighbor)
        
        result = []
        # loop through ancestor dict -> append values to result
        for i in range(n):
            result.append(sorted(list(ancestors[i])))

        return result