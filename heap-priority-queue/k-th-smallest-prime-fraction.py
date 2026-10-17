class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        fraction = []

        n = len(arr)
        for i in range(n - 1):
            heapq.heappush(fraction, (arr[i] / arr[-1], i, n - 1))
        
        for _ in range(k - 1):
            _, i, j = heapq.heappop(fraction)
            
            # if not enough pairs
            if j - 1 > i:
                heapq.heappush(fraction, (arr[i] / arr[j - 1], i, j - 1))
        
        _, i, j = heapq.heappop(fraction)
        return [arr[i], arr[j]]