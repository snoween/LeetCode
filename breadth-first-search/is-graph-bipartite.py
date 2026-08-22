class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        color = [0] * n

        for i in range(n):
            if color[i] == 0:
                color[i] = 1
                queue = deque([i])

                while queue:
                    curr = queue.popleft()

                    for neighbor in graph[curr]:
                        # if next vertex has same val -> return false
                        if color[neighbor] == color[curr]:
                            return False
                        
                        if color[neighbor] == 0:
                            color[neighbor] = -color[curr]
                            queue.append(neighbor)
        
        return True