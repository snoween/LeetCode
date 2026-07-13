class SmallestInfiniteSet:

    def __init__(self):
        self.set_inf = set(list(range(1, 1001)))
        self.heap = list(range(1, 1001))
        heapq.heapify(self.heap)

    def popSmallest(self) -> int:
        del_num = heapq.heappop(self.heap)
        if del_num in self.set_inf:
            self.set_inf.remove(del_num)
        return del_num

    def addBack(self, num: int) -> None:
        if num not in self.set_inf:
            self.set_inf.add(num)
            heapq.heappush(self.heap, num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)