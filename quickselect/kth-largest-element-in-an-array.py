class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        numsNegative = [-num for num in nums]
        heapq.heapify(numsNegative)

        for _ in range(k):
            result = heapq.heappop(numsNegative)
        
        return -result