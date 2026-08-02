# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        # define queue to store root as initial val
        queue = deque()
        queue.append(root)
        # define output array as empty
        output = []

        # loop while queue is valid
        while queue:
            # get len of current queue
            n = len(queue)
            # define empty layer array
            layer = []

            # loop through len queue
            for _ in range(n):
                # popleft the node
                node = queue.popleft()
                # layer append node value
                layer.append(node.val)
                # check if node left
                if node.left:
                    # append node left to queue
                    queue.append(node.left)
                # check if node right
                if node.right:
                    # append node right to queue
                    queue.append(node.right)
            
            # output append layer
            output.append(layer)
        
        # return output
        return output