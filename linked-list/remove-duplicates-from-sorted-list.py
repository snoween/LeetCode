# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 1 -> 1 -> 1 -> 2
        # loop 1: equal prev = 1 [0], curr = head.next = 1 [1]
        # loop 2: equal: prev = 1[0], curr = 1 [2]
        # loop 3: no equal prev = 1 [0], curr = 2 [3] -> update prev = 2
        # output: 1 -> 2

        if not head:
            return None
        
        prev = head
        curr = head.next

        while curr:
            if prev.val == curr.val:
                prev.next = curr.next
            else:
                prev = curr

            curr = curr.next

        prev.next = None
        return head