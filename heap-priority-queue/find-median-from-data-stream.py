class MedianFinder:

    def __init__(self):
        self.heap_min = []
        self.heap_max = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.heap_max, -num)

        max_num = heapq.heappop(self.heap_max)
        heapq.heappush(self.heap_min, -max_num)

        if len(self.heap_min) > len(self.heap_max):
            min_num = heapq.heappop(self.heap_min)
            heapq.heappush(self.heap_max, -min_num)

    def findMedian(self) -> float:
        if len(self.heap_min) == len(self.heap_max):
            return ((self.heap_min[0] - (self.heap_max[0])) / 2)
        else:
            return -self.heap_max[0]
   

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()