# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        curr = dummy
        curr2 = dummy
        
        for _ in range(n+1):
            curr = curr.next
        
        while curr:
            curr2 = curr2.next
            curr = curr.next

        curr2.next = curr2.next.next

        return dummy.next
