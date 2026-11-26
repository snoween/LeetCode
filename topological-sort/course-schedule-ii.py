class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        """
        Solution: topo sort
        1. Build graph, in degree
        2. Build queue
        3. BFS through queue. Append the node to result array after popleft from queue
        To check if cannot complete all courses or not -> check if cycle, or count = numCourses or not
        """
        # build graph
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
        
        # BFS through queue
        result = []

        while queue:
            curr_node = queue.popleft()
            result.append(curr_node)

            for adj in graph[curr_node]:
                in_degree[adj] -= 1
                if in_degree[adj] == 0:
                    queue.append(adj)
        
        return result if len(result) == numCourses else []