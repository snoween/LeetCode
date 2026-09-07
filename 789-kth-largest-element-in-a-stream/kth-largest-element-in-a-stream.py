class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.scores = []
        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        heapq.heappush(self.scores, val)
        
        # only save k nums in scores
        if len(self.scores) > self.k:
            heapq.heappop(self.scores)
        
        return self.scores[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)