# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Order: Root -> Left -> Right
        if not root:
            return []
        
        result = [root.val]

        # Check if node left to avoid appending None value -> save some space 
        if root.left:
            result.extend(self.preorderTraversal(root.left))
        
        # Similarly checking for right node
        if root.right:
            result.extend(self.preorderTraversal(root.right))

        return result