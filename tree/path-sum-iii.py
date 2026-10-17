# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode | None, targetSum: int) -> int:
        # save freq of all total
        prefix_sum = {0: 1}
        
        def backtrack(node, curr_sum):
            if not node:
                return 0
            
            curr_sum += node.val
            target = curr_sum - targetSum
            valid_path = prefix_sum.get(target, 0)

            prefix_sum[curr_sum] = prefix_sum.get(curr_sum, 0) + 1

            # backtrack left + right
            valid_path += backtrack(node.left, curr_sum)
            valid_path += backtrack(node.right, curr_sum)

            # undo
            prefix_sum[curr_sum] -= 1
            return valid_path
        
        return backtrack(root, 0)

