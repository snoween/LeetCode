# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode | None) -> list[str]:
        """ 
        path [1]
        check if 1 is leaf -> F
        -> continue with left node
        -> path = [1 2]
        backtrack(2) -> 2 is not leaf 
        -> path = [1 2 5]
        backtrack(5)
        -> 5 is leaf -> record path -> undo
        -> path = [1]
        -> continue with right node
        -> path = [1 3]
        -> backtrack(3) -> 3 is leaf -> record result
        Time comp: O(N)
        Space comp: O(N)
        """
        if not root:
            return []

        result = []
        path = []

        def backtrack(node):
            path.append(str(node.val))
            
            if not node.left and not node.right:
                result.append('->'.join(path))
            else:
                if node.left:
                    backtrack(node.left)
                if node.right:
                    backtrack(node.right)
            path.pop()
        
        backtrack(root)
        return result
