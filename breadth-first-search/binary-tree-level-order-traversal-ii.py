# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        # queue append root
        queue = deque()
        queue.append(root)
        # set init output = []
        output = []

        # loop while valid queue
        while queue:
            # get len queue
            n = len(queue)
            # set layer = []
            layer = []
            # loop through len
            for _ in range(n):
                # popleft queue
                node = queue.popleft()
                # layer append node val
                layer.append(node.val)
                # if node left -> append to queue
                if node.left:
                    queue.append(node.left)
                # if node right -> append to queue
                if node.right:
                    queue.append(node.right)
            
            # output append layer
            output.append(layer)
        
        # return reversed output
        return output[::-1]
