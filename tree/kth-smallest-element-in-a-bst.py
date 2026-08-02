# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # BFS
        # queue to store node
        queue = deque()
        # queue append root
        queue.append(root)
        # heap to store min value
        heap = []
        # while loop until not queue
        while queue:
            # get len queue to check how many nodes at current time
            n = len(queue)
            # loop through all nodes in range len
            for _ in range(n):
                # popleft queue to get left most node
                node = queue.popleft()
                # push val to heap
                heapq.heappush(heap, node.val)
                # if node left
                if node.left:
                    # queue append node left
                    queue.append(node.left)
                # if node right
                if node.right:
                    # queue append node right
                    queue.append(node.right)
        
        output = 0
        # loop through k times
        for _ in range(k):
            # heap pop val after k times
            output = heapq.heappop(heap)
        
        # return output val
        return output