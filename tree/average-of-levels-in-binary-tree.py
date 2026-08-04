# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
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
            # set init sum_layer = 0
            sum_layer = 0
            # loop through len
            for _ in range(n):
                # popleft to get node
                node = queue.popleft()
                # update sum_layer += node val
                sum_layer += node.val
                # if node left -> append to queue
                if node.left:
                    queue.append(node.left)
                # if node right -> append to queue
                if node.right:
                    queue.append(node.right)
            
            # append avg to output: avg = sum_layer / n
            output.append(sum_layer / n)
        
        # return output
        return output
        