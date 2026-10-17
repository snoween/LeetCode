# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        tree = []

        def inorder(node):
            if not node:
                return None
            inorder(node.left)
            tree.append(node.val)
            inorder(node.right)
        
        inorder(root)
        
        left, right = 0, len(tree) - 1

        while left < right:
            curr_sum = tree[left] + tree[right]
            
            if curr_sum == k:
                return True
            elif curr_sum < k:
                left += 1
            else:
                right -= 1
        
        return False