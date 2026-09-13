class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        """
        Method: use color array to check
        """
        n = len(graph)
        color = [0] * n

        for i in range(n):
            if color[i] == 0:
                color[i] = 1
                queue = deque([i])

                while queue:
                    curr = queue.popleft()
                    for neighbor in graph[curr]:
                        if color[neighbor] == color[curr]:
                            return False
                        
                        if color[neighbor] == 0:
                            color[neighbor] = -color[curr]
                            queue.append(neighbor)
        
        return True