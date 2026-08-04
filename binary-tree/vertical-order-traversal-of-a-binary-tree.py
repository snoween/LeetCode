# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        # set init queue -> append tuple ((0, 0), root)
        queue = deque()
        queue.append(((0, 0), root))
        # set intit heap = []
        heap = []

        # loop while valid queue
        while queue:
            # get len queue
            n = len(queue)
            # loop through len
            for _ in range(n):
                # popleft node
                coor, node = queue.popleft()
                # heappush to output based on second ele of tuple
                heapq.heappush(heap, (coor, node.val))
                # if node left -> append tuple ((node_c - 1, node_r + 1), node left)
                if node.left:
                    queue.append(((coor[0] - 1, coor[1] + 1), node.left))

                # if node right -> append tuple ((node_c + 1, node_r - 1), node right)
                if node.right:
                    queue.append(((coor[0] + 1, coor[1] + 1), node.right))
                   
        idx_val = defaultdict(list)
        while heap:
            ele  = heapq.heappop(heap)
            idx_val[ele[0][0]].append(ele[1])
        
        output = []
        for key in sorted(idx_val.keys()):
            output.append(idx_val[key])
        
        return output