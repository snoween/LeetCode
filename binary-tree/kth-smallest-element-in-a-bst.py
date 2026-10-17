# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode | None, k: int) -> int:
        if not root:
            return 0
        
        queue = deque([root])
        pq = []

        while queue:
            node = queue.popleft()
            heapq.heappush(pq, node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        for _ in range(k):
            output = heapq.heappop(pq)
        
        return output