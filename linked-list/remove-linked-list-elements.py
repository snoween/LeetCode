# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        curr = head

         # loop nay de tim node dau tien co gia tri khac k
        while curr and  curr.val == k:
            curr = curr.next

        if not head:
            return None

        if not curr:
            return None
        
        # khi minh return, minh se return node do
        output = curr 

        # minh can fai remove nhung node co gia tri k trong phan con lia cua linkedlist tu curr di xuong

        prev = curr

        while prev.next:
            curr = prev.next
            if curr.val == k:
                prev.next = curr.next
            else:
                prev = curr

        return output