class MedianFinder:

    def __init__(self):
        self.count = 0
        self.pref_sum = 0

    def addNum(self, num: int) -> None:
        self.pref_sum += num
        self.count += 1

    def findMedian(self) -> float:
        return self.pref_sum / self.count


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()