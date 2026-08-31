class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = defaultdict(list)
        in_degree = defaultdict(int)

        for preq, course in prerequisites:
            adj[preq].append(course)
            in_degree[course] += 1

        queue = deque()
        for i in range(numCourses):
            if in_degree[i] == 0:
                queue.append(i)
        
        prereq = [set() for _ in range(numCourses)]
        while queue:
            curr = queue.popleft()

            for neighbor in adj[curr]:
                in_degree[neighbor] -= 1
                prereq[neighbor].add(curr)
                prereq[neighbor].update(prereq[curr])

                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        ans = []
        for preq, course in queries:
            ans.append(preq in prereq[course])
        
        return ans