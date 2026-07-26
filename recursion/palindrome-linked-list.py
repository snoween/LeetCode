# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        size = 0
        dummy = head
        while head:
            size += 1
            head = head.next
        
        stack = []
        half = size // 2
        while size > 0:
            stack.append(dummy.val)
            dummy = dummy.next
            size -= 1
        
            while dummy and 0 <= size <= half:
                if stack and dummy.val != stack.pop():
                    return False
                dummy = dummy.next
                size -= 1
        
        return True
            