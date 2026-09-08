# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        queue = deque([root])
        left_sum = 0

        while queue:
            curr = queue.popleft()
            if curr.left:
                queue.append(curr.left)
                left_sum += curr.left.val
            if curr.right:
                queue.append(curr.right)
        
        return left_sum