class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """
        - Method: DFS (3 states)
        - Time comp: O(V + E)
        - Space comp: O(V + E)
        """
        # build graph
        #[a, b]: b -> a node b : list(a)
        adj = defaultdict(list)
        # build in degree
        in_degree = defaultdict(int)
        for course, preq in prerequisites: 
            adj[preq].append(course)
            # in degree -> dict 
            in_degree[course] += 1
        
        queue = deque()
        for i in range(numCourses):
            if in_degree[i] == 0:
                queue.append(i)
        
        result = []

        while queue:
            curr = queue.popleft()
            result.append(curr)

            for neighbor in adj[curr]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        return result