class Solution:
    def maximumCoins(self, coins: List[List[int]], k: int) -> int:
        coins.sort()
        n = len(coins)
        res = 0
        total = 0
        right = 0

        for left in range(n):
            end = coins[left][0] + k  

            while right < n and coins[right][1] < end:
                l, r, c = coins[right]
                total += (r - l + 1) * c
                right += 1

            extra = 0
            if right < n and coins[right][0] < end:
                l, r, c = coins[right]
                extra = (min(end, r + 1) - l) * c

            res = max(res, total + extra)

            l, r, c = coins[left]
            if right > left:
                total -= (r - l + 1) * c
                right = max(right, left + 1)

        return res
