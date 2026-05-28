# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None
        length = 1
        count = 1

        while curr.next:
            length += 1
            curr = curr.next
        
        curr = head
        while count != (length // 2):
            curr = curr.next
            count += 1
        
        return curr.next
