# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Inorder: Left -> root -> Right
        if not root:
            return []
        
        result = []

        # Check if root.left -> avoid call stack None to save some space -> extend call stack memory
        if root.left:
            result.extend(self.inorderTraversal(root.left))
        
        # Append root value
        result.append(root.val)

        # Check if node right -> avoid call stack None to save some space -> extend call stack memory
        if root.right:
            result.extend(self.inorderTraversal(root.right))
        
        return result
            