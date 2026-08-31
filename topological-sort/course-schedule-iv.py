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
        
        list_courses = []
        while queue:
            curr = queue.popleft()
            list_courses.append(curr)

            for neighbor in adj[curr]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        ans = []
        for preq, course in queries:
            if list_courses[preq] < list_courses[course]:
                ans.append(True)
            else:
                ans.append(False)
        
        return ans