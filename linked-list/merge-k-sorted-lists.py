# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # [[1,4,5],[1,3,4],[2,6]]

        # (1, 0), (1, 1), (2, 2)  
        dummy = ListNode()
        tail = dummy

        heap = []
        for i, head in enumerate(lists):
            if head:
                heap.append((head.val, i))
        
        while heap:
            _, index = heapq.heappop(heap)
            tail.next = lists[index]
            tail = tail.next

            lists[index] = lists[index].next

            if lists[index]:
                heapq.heappush(heap, (lists[index].val, index))
        
        return dummy.next