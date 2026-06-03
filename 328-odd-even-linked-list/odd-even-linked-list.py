# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy_odd = ListNode()
        dummy_even = ListNode()

        curr_odd = dummy_odd
        curr_even = dummy_even
        head_even = curr_even

        index = 1
        while head:
            if index % 2 != 0:
                curr_odd.next = head
                curr_odd = curr_odd.next
            
            else:
                curr_even.next = head
                curr_even = curr_even.next
            
            head = head.next
            index += 1
        
        curr_odd.next = head_even.next
        curr_even.next = None

        return dummy_odd.next