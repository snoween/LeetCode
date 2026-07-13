# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 1 -> 1 -> 2
        # curr = 1, curr.next = next = 1
        # if next = curr: curr -> curr.next.next

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