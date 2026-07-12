class Solution:
    def maximumCoins(self, coins: List[List[int]], k: int) -> int:
        def slide(segs):
            segs = sorted(segs)
            n = len(segs)
            res = 0
            total = 0
            right = 0

            for left in range(n):
                end = segs[left][0] + k

                while right < n and segs[right][1] < end:
                    l, r, c = segs[right]
                    total += (r - l + 1) * c
                    right += 1

                extra = 0
                if right < n and segs[right][0] < end:
                    l, r, c = segs[right]
                    extra = (min(end, r + 1) - l) * c

                res = max(res, total + extra)

                l, r, c = segs[left]
                if right > left:
                    total -= (r - l + 1) * c
                    right = max(right, left + 1)

            return res

        # Case 1: window starts at random l_i 
        case1 = slide(coins)
        # Case 2: windows ends at random r_i
        case2 = slide([[-r, -l, c] for l, r, c in coins])

        return max(case1, case2)
