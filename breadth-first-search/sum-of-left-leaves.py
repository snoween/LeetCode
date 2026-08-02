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
        
        # queue and append root
        queue = deque()
        queue.append(root)
        # left sum = 0
        sumLeft = 0

        # loop while queue is valid
        while queue:
            # get len queue
            n = len(queue)
            # loop through len queue
            for _ in range(n):
                # pop node
                node = queue.popleft()
                
                # if node left:
                if node.left:
                    # update left sum += node left val
                    sumLeft += node.left.val
                    # append node to queue
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        # return left sum
        return sumLeft