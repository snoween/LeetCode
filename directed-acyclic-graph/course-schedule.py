class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        - Solution: DFS
        - Time comp: O(V + E)
        - Sapce comp: O(V + E)
        """
        # set init adj to store node and its neighbors
        adj = defaultdict(list)
        for course, preq in prerequisites:
            adj[preq].append(course)
        # set list of visit with [0] elements = num course
        visit = [0] * numCourses
        # set result = []
        result = []

        # func DFS on a node, return bool
        def dfs(node) -> bool:
            # state: 0: not visit; 1: visiting; 2: visited
            # check state of the node
            # if state = 1 -> has cycle -> return False
            if visit[node] == 1:
                return False

            # if state = 2 -> done checking this neighbor -> return True
            if visit[node] == 2:
                return True

            # if state = 0 -> not visit -> change to state 1
            visit[node] = 1

            # loop all neighbors of that node
            for neighbor in adj[node]:
                # check if not DFS(neighbor) -> cycle -> return False
                if not dfs(neighbor):
                    return False
            
            # if all neighbors are fine -> change state of current node to 2 - done
            visit[node] = 2

            # append that node to result
            result.append(node)

            # return True
            return True
        
        # loop through all courses
        for i in range(numCourses):
            # if visit = 0 -> call DFS
            if visit[i] == 0:
                # if not dfs(i) -> has cycle -> return False
                if not dfs(i):
                    return False
        
        # return True
        return True