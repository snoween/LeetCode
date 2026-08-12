# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if not root1 or not root2:
            return False

        def getLeaf(root: Optional[TreeNode]):
            if not root:
                return None
            
            if not root.left and not root.right:
                return [root.val]

            result = []
            if root.left:
                result.extend(getLeaf(root.left))
            if root.right:
                result.extend(getLeaf(root.right))
            return result

        return getLeaf(root1) == getLeaf(root2)