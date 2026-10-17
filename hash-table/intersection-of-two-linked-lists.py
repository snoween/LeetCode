# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA or not headB:
            return None

        pointer_A = headA
        pointer_B = headB

        while pointer_A != pointer_B:
            pointer_A = pointer_A.next if pointer_A else headB
            pointer_B = pointer_B.next if pointer_B else headA
        
        return pointer_A