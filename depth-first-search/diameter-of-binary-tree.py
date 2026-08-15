# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def findMaxHeight(root: Optional[TreeNode]) -> int:
            if not root:
                return 0
            
            return 1 + max(findMaxHeight(root.left), findMaxHeight(root.right))
        
        if not root:
            return 0
        
        diameter = 0

        if root.left:
            diameter += findMaxHeight(root.left)
        if root.right:
            diameter += findMaxHeight(root.right)
        
        return diameter