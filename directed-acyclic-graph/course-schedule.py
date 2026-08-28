class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        - Solution: BFS - Kahn's algorithm
        - Time comp: O(N x 2)
        - Sapce comp: O(N x 2)
        """
        # set init adj to store node and its neighbors
        adj = defaultdict(list)
        # set in_degree as list of 0 to calculate edges of nodes
        in_degree = [0] * numCourses

        # loop through prerequisites to update adj and in_degree
        for course, pre in prerequisites:
            # key = bi, val = ai
            adj[pre].append(course)
            # in_degree[ai] += 1 -> ai has +1 edge
            in_degree[course] += 1
        
        # loop through in_degree, if 0 edge -> append index = node val to queue
        queue = deque()
        for i, edge in enumerate(in_degree):
            if edge == 0:
                queue.append(i)

        # result = []
        result = []
        # loop while valid queue
        while queue:
            # get current node = popleft
            curr = queue.popleft()
            # append current node to result
            result.append(curr)

            # loop through all neighbors of that current node
            for neighbors in adj[curr]:
                # in_degree of that neighbor is decreased by 1
                in_degree[neighbors] -= 1
                # if that in_degree is 0 edge -> append to queue
                if in_degree[neighbors] == 0:
                    queue.append(neighbors)
        
        # check if len result = num course -> valid output
        return (len(result) == numCourses)
            