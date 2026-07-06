class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        # heap -> [-100 -64 -25 -9 -4]
        # k iterations
        # First iteration
        # Pop sqrt(100) --> Push back: [-64 -25 -10 -9 -4]
        # Second iteration
        # Pop sqrt(-64) --> Push back: [-25 -10 -8 -9 -4]

        gifts_minus = [-num for num in gifts]
        heapq.heapify(gifts_minus)

        for i in range(k):
            if gifts_minus:
                remaining = int(math.sqrt(-heapq.heappop(gifts_minus)))
                heapq.heappush(gifts_minus, -remaining)

        return -sum(gifts_minus)