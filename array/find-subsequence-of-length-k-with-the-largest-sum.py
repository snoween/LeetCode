class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        # Pop until the list has k elements -> sort result by index
        nums_heap = []
        for i, num in enumerate(nums):
            nums_heap.append([num, i])
        heapq.heapify(nums_heap)

        while len(nums_heap) > k:
            heapq.heappop(nums_heap)
           
        return [item[0] for item in sorted(nums_heap, key=lambda x: x[1])]