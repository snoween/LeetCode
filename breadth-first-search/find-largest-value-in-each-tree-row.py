# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        # queue append root
        queue = deque()
        queue.append(root)
        # set output = []
        output = []
        
        # loop while valid queue
        while queue:
            # get len queue
            n = len(queue)
            # set max val = -inf
            max_val = -inf
            # loop through len queue
            for _ in range(n):
                # popleft node
                node = queue.popleft()
                # update max val = max(max val, node val)
                max_val = max(max_val, node.val)
                # if node left -> append to queue
                if node.left:
                    queue.append(node.left)
                # if node right -> append to queue
                if node.right:
                    queue.append(node.right)
            
            # append max val to output
            output.append(max_val)
        
        # return output
        return output