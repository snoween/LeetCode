class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        fraction = []

        for i, num in enumerate(arr):
            for j in range(i + 1, len(arr)):
                fraction.append((num / arr[j], (num, arr[j])))
        
        heapq.heapify(fraction)
        pair = []
        for _ in range(k):
            _, pair = heapq.heappop(fraction)
        
        return list(pair)