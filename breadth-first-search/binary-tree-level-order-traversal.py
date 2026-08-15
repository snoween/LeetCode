# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        - Do they need layer checking? - Yes
        - Algorithm: BFS, queue
        - Time comp: O(N)
        - Space comp: O(N)
        """
        if not root:
            return []
        
        # Get a deque with root
        queue = deque()
        queue.append(root)

        # init result as []
        result = []

        # check while valid queue
        while queue:
            # get len recent queue
            n = len(queue)
            # set init layer = []
            layer = []
            # for loop through len queue
            for _ in range(n):
                # pop queue to get node
                node = queue.popleft()
                # layer append node val
                layer.append(node.val)
                # check if node left -> append to queue
                if node.left:
                    queue.append(node.left)
                # check if node right -> append to queue
                if node.right:
                    queue.append(node.right)
            
            # append layer to result
            result.append(layer)
        
        # return result
        return result
