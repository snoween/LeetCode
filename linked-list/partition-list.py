# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy_left = ListNode()
        dummy_right = ListNode()

        curr_left = dummy_left
        curr_right = dummy_right

        head_right = curr_right

        while head:
            if head.val < x:
                curr_left.next = head
                curr_left = curr_left.next
            
            else:
                curr_right.next = head
                curr_right = curr_right.next
            
            head = head.next
        
        curr_left.next = head_right.next
        curr_right.next = None

        return dummy_left.next