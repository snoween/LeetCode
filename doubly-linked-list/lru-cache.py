class ListNode:
    def __init__(self):
        self.key = 0
        self.val = 0
        self.next = None
        self.prev = None
        
 
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.current_capacity = 0

        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.meet = {} # key:int value: ListNode

    def get(self, key: int) -> int:
        if key not in self.meet:
            return -1
        
        node = self.meet[key]

        node_next = node.next
        node_prev = node.prev
        node_next.prev = node_prev
        node_prev.next = node_next

        head_next = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = head_next
        head_next.prev = node

        return node.val

    def put(self, key: int, value: int) -> None:
        # new entry
        if key not in self.meet:
            self.meet[key] = ListNode()
            self.current_capacity += 1
            if self.current_capacity > self.capacity:
                del self.meet[self.tail.prev.key]

                prevNode = self.tail.prev.prev
                self.tail.prev = prevNode
                prevNode.next = self.tail

                self.current_capacity -= 1
        else:
            prevNode = self.meet[key].prev
            nextNode = self.meet[key].next
            prevNode.next = nextNode
            nextNode.prev = prevNode

        
        newNode = self.meet[key]
        newNode.val = value
        newNode.key = key
        
        newNode.next = self.head.next
        self.head.next = newNode
        newNode.prev = self.head
        newNode.next.prev = newNode

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)