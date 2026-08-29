class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        - Solution: DFS
        - Time comp: O(V + E)
        - Sapce comp: O(V + E)
        """
         # build graph 
        adj = defaultdict(list)
        in_degree = defaultdict(int)

        for course, preq in prerequisites:
            adj[preq].append(course)
            in_degree[course] += 1

        queue = deque()
        for i in range(numCourses):
            if in_degree[i] == 0:     
                queue.append(i)     
        
        count = 0

        while queue:
            curr = queue.popleft()
            count += 1

            for neighbor in adj[curr]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        return count == numCourses