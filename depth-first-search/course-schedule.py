class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        """
        Solution: topo sort
        1. build graph
        2. build queue
        3. BFS for adj nodes
        """
        # Build graph for DAG: b -> a
        graph = defaultdict(list)
        in_degree = defaultdict(int)
        for a, b in prerequisites:
            graph[b].append(a)
            in_degree[a] += 1
        
        # build queue
        queue = deque()
        for i in range(numCourses):
            if in_degree[i] == 0:
                queue.append(i)
        
        # BFS
        count = 0
        while queue:
            curr_node = queue.popleft()
            count += 1

            for adj in graph[curr_node]:
                in_degree[adj] -= 1
                if in_degree[adj] == 0:
                    queue.append(adj)
        
        return count == numCourses