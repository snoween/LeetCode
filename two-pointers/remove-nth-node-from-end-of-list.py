# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Get the length of list node
        def get_length(node):
            count = 1
            while node.next != None:
                count += 1
                node = node.next
            return count
        
        length_head = get_length(head)
        if length_head == n:
            return head.next

        curr = head
        prev = None
        # Remove the nth if the index of that node is length - current length = n
        while curr:
            next_node = curr.next
            prev = curr
            curr = next_node
            length_head -= 1
            
            if length_head == n:
                prev.next = curr.next
            
        return head
