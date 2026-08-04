# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        queue = deque()
        queue.append(root)
        level = 1
        output = []

        while queue:
            n = len(queue)
            layer = []
            for _ in range(n):
                node = queue.popleft()
                layer.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            if level % 2 == 0:
                output.append(layer[::-1])
            else:
                output.append(layer)
            
            level += 1
        
        return output