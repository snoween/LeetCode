class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """
        - Method: DFS (3 states)
        - Time comp: O(V + E)
        - Space comp: O(V + E)
        """

        # set up the adjacent dictionary, with key = prereq, val = course
        adj = defaultdict(list)
        for course, prereq in prerequisites:
            adj[prereq].append(course)

        # set up list visit with numCourses elements of 0
        visit = [0] * numCourses

        # empty list result to store courses
        result = []

        # dfs function to check state of a node -> return bool
        def dfs(node) -> bool:
            # 0: not visit; 1: visiting; 2: visited
            # Check state of the node
            # If state is 1 -> has cycle -> return False
            if visit[node] == 1:
                return False

            # if state is 2 -> done visiting -> return True
            if visit[node] == 2:
                return True

            # if state is 0 -> not visit -> change state to 1
            visit[node] = 1

            # loop through all neighbors of current node
            for neighbor in adj[node]:
                # if that neighbor has cycle -> return False
                if not dfs(neighbor):
                    return False
            
            # if all neighbors are valid -> change state of current node to 2
            visit[node] = 2

            # append that node to result
            result.append(node)

            # return True
            return True
        
        # loop through all courses
        for i in range(numCourses):
            # check if the state in visit of that course
            # if not valid state -> has cycle -> return []
            if visit[i] == 0:
                if not dfs(i):
                    return []
        
        # return reverse result - bc DFS returns nodes from end -> start
        result.reverse()
        return result