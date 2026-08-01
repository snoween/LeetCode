# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
            
        queue = deque()
        queue.append((root, -inf, inf))

        while queue:
            root, lower, upper = queue.popleft()

            if root.val < lower or root.left > upper:
                return False
            
            if not root.left:
                queue.append((root.left, lower, root.val))
            
            if not root.right:
                queue.append((root.right, root.val, upper))
        
        return True