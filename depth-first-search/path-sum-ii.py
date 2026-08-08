# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        
        stack = [(root, root.val, [root.val])]
        output = []

        while stack:
            node, curr_sum, path = stack.pop()
            if not node.left and not node.right and curr_sum == targetSum:
                output.append(path)
            
            if node.left:
                path_copy = path[:]
                path_copy.append(node.left.val)
                stack.append((node.left, curr_sum + node.left.val, path_copy))
            
            if node.right:
                path_copy = path[:]
                path_copy.append(node.right.val)
                stack.append((node.right, curr_sum + node.right.val, path_copy))
        
        return output