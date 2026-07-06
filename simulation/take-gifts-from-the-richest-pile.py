class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        # heap -> [-100 -64 -25 -9 -4]
        # k iterations
        # gifts remaining += heap(0)

        gifts_minus = [-num for num in gifts]
        heapq.heapify(gifts_minus)

        for i in range(k):
            if gifts_minus:
                remaining = int(math.sqrt(-heapq.heappop(gifts_minus)))
                heapq.heappush(gifts_minus, -remaining)

        return -sum(gifts_minus)