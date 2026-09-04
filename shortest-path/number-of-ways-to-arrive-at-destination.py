class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        # build graph with weight of each node

        # build dist for all nodes = inf

        # push to heap the node has dist = 0 (starting node = 0)

        # build a function môn stack to check current path from 0 - n-1 has smaller val or not
        # loop while valid heap
            # get curr dist, curr node = heappop

            # push curr dist to result
            # if curr dist > dist[node] -> continue

            # loop through node neighbors 
                # check if curr dist + weight < dist[negihbor]
                    # replace dist[neighbor]
                    # push dist neighbor, neighbor to heap

        # set count = 1

        # curr min = heappop result

        # loop while heappop result = curr min -> count + 1