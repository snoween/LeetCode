class MedianFinder:

    def __init__(self):
        self.heap_min = []
        self.heap_max = []
        self.med_val = 0
        self.prev = 0

    def addNum(self, num: int) -> None:
        print(num)
        if not self.heap_min and not self.heap_max:
            self.heap_min.append(num)
        elif num >= self.heap_min[-1]:
            self.heap_max.append(num)
        else:
            self.heap_min.append(num)
        print(self.heap_min)
        print(self.heap_max)

    def findMedian(self) -> float:
        heapq.heapify(self.heap_min)
        heapq.heapify(self.heap_max)
    
        if len(self.heap_min) - len(self.heap_max) == 0:
            return (self.heap_min[-1] + (self.heap_max[0])) / 2
        elif len(self.heap_min) - len(self.heap_max) == 1:
            return self.heap_min[-1]
        elif len(self.heap_min) - len(self.heap_max) == -1:
            return self.heap_max[0]
        
        elif len(self.heap_min) - len(self.heap_max) == 2:
            return (self.heap_min[0] + self.heap_min[1]) / 2
        elif len(self.heap_min) - len(self.heap_max) == -2:
            return (self.heap_max[0] + self.heap_max[1]) / 2
        

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()