class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        freq = Counter(nums)
        
        pq = []
        for key, val in freq.items():
            heapq.heappush(pq, (-val, key))
        
        result = []
        for _ in range(k):
            _, digit = heapq.heappop(pq)
            result.append(digit)
        
        return result