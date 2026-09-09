class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        piles_max = [-num for num in piles]

        heapq.heapify(piles_max)
        for _ in range(k):
            curr = heapq.heappop(piles_max)
            heapq.heappush(piles_max, curr // 2)
        
        return -sum(piles_max)