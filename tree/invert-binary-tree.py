# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        queue = deque()
        queue.append(root)

        while queue:
            n = len(queue)
            for _ in range(n):
                node = queue.popleft()
                if node.right and node.left:
                    node.right, node.left = node.left, node.right
                    queue.append(node.left)
                    queue.append(node.right)
                if node.left and not node.right:
                    queue.append(node.left)
                if node.right and not node.left:
                    queue.append(node.right)
        
        return root
                