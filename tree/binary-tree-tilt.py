# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        def _sum(root):
            if not root:
                return 0
            return _sum(root.left) + _sum(root.right) + root.val
        
        if not root:
            return 0
        tilt = abs(_sum(root.left) - _sum(root.right))
        return self.findTilt(root.left) + self.findTilt(root.right) + tilt

        
        