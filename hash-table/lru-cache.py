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
        self.removeNode(node)
        self.insertAtHead(node)

        return node.val

    def put(self, key: int, value: int) -> None:
        # new entry
        if key not in self.meet:
            self.meet[key] = ListNode()
            self.current_capacity += 1
            if self.current_capacity > self.capacity:
                del self.meet[self.tail.prev.key]
                self.removeNode(self.tail.prev)
                self.current_capacity -= 1
        else:
            self.removeNode(self.meet[key])
        
        newNode = self.meet[key]
        newNode.val = value
        newNode.key = key
        self.insertAtHead(newNode)


    def removeNode(self, node):
        node_next = node.next
        node_prev = node.prev
        node_next.prev = node_prev
        node_prev.next = node_next

    def insertAtHead(self, node):
        head_next = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = head_next
        head_next.prev = node  


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)