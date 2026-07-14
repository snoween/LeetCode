class MedianFinder:

    def __init__(self):
        self.heap_min = []
        self.heap_max = []
        self.med_val = 0
        self.prev = 0

    def addNum(self, num: int) -> None:
        if not self.heap_min and not self.heap_max:
            self.heap_min.append(num)
        elif num >= self.heap_min[-1]:
            self.heap_max.append(-num)
        elif num < self.heap_max[-1]:
            self.heap_min.append(num)
            
    def findMedian(self) -> float:
        heapq.heapify(self.heap_min)
        heapq.heapify(self.heap_max)
        print(self.heap_min)
        print(self.heap_max)
        
        if len(self.heap_min) - len(self.heap_max) == 0:
            return (self.heap_min[-1] + (-self.heap_max[-1])) / 2
        elif len(self.heap_min) > len(self.heap_max):
            return self.heap_min[-1]
        elif len(self.heap_min) < len(self.heap_max):
            return -self.heap_max[-1]

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()