# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        # even idx: increasing
        # odd idx: decreasing
        if not root:
            return False
        
        # queue and append root
        queue = deque()
        queue.append(root)
        # set init idx = 0
        index = 1

        # loop while valid queue
        while queue:
            # get len queue
            n = len(queue)
            # set prev = none
            prev = None
            # loop through len queue
            for _ in range(n):
                # popleft node
                curr = queue.popleft()
                
                # if not prev
                if not prev:
                    # prev = node (first node in queue)
                    prev = curr
                    # check if the first node is valid or not
                    if index % 2 == 0 and prev.val % 2 != 0:
                        return False
                    elif index % 2 != 0 and prev.val % 2 == 0:
                        return False
                # else
                else:
                    # if odd idx
                    if index % 2 == 0:
                        # if node > prev
                        if curr.val >= prev.val or curr.val % 2 != 0:
                            # return false
                            return False
                    # if even idx
                    else:
                        # if node < prev
                        if curr.val <= prev.val or curr.val % 2 == 0:
                            # return false
                            return False
                    
                # if node left -> append to queue
                if curr.left:
                    queue.append(curr.left)
                # if node right -> append to queue
                if curr.right:
                    queue.append(curr.right)

                # update prev to curr
                prev = curr
                
            # update index
            index += 1

        # return true if pass all layers
        return True