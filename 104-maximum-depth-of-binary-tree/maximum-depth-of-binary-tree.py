# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        # queue append root
        queue = deque()
        queue.append(root)
        # set init depth = 1
        depth = 1

        # loop while valid queue
        while queue:
            # get len queue
            n = len(queue)
            # loop through len
            for _ in range(n):
                # popleft queue
                node = queue.popleft()
                # if node left -> append to queue
                if node.left:
                    queue.append(node.left)
                # if node right -> append to queue
                if node.right:
                    queue.append(node.right)
            
            # increase depth by 1
            depth += 1
        
        # return depth, offset by 1
        return depth - 1