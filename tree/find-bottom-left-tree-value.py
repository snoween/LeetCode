# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        queue = deque([root])

        while queue:
            curr = queue.popleft()
            if curr.left:
                queue.append(curr.left)
                if not curr.left.left and not curr.left.right:
                    leftmost = curr.left.val
            
            if curr.right:
                queue.append(curr.right)
        
        return leftmost