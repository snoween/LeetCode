# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        # set init queue, append root to queue
        queue = deque()
        queue.append(root)
        # set init output = []
        output = []

        # loop while valid queue
        while queue:
            # get len queue
            n = len(queue)
            # loop through len
            for i in range(n):
                # popleft node
                node = queue.popleft()
                # if node left -> append to queue
                if node.left:
                    queue.append(node.left)
                # if node right -> append to queue
                if node.right:
                    queue.append(node.right)
            
            # append val node to output, because now node = last node in queue
            output.append(node.val)    
        
        # return output
        return output