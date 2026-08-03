# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        # queue append root
        queue = deque()
        queue.append(root)
        # min depth = 1
        min_depth = 1

        # loop while valid queue
        while queue:
            # get len queue
            n = len(queue)
            # loop through len queue
            for _ in range(n):
                # popleft node
                node = queue.popleft()
                # if not node right and left
                if not node.left and not node.right:
                    # return min depth
                    return min_depth
                # if node left -> append to queue
                if node.left:
                    queue.append(node.left)
                # if node right -> append to queue
                if node.right:
                    queue.append(node.right)
            
            # min depth += 1
            min_depth += 1
        
        # 
                    