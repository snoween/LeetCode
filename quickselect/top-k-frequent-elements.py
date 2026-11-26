class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        freq = Counter(nums)
        heap = [(-val, key) for key, val in freq.items()]
        heapq.heapify(heap)

        result = []
        for _ in range(k):
            _, num = heapq.heappop(heap)
            result.append(num)
        
        return result