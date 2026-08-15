# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # order: Left -> Right -> root
        if not root:
            return []
        
        result = []

        # check if left node to avoid None val -> save space
        if root.left:
            result.extend(self.postorderTraversal(root.left))
        
        # similarly for right node
        if root.right:
            result.extend(self.postorderTraversal(root.right))
        
        # append root val
        result.append(root.val)

        return result
