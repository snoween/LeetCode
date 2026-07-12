class Solution:
    def maximumCoins(self, coins: List[List[int]], k: int) -> int:
        def bestTotal(segments):
            segments.sort()
            n = len(segments)

            best = 0
            window_sum = 0  
            j = 0            

            for i in range(n):
                l_i, r_i, c_i = segments[i]
                window_start = r_i - k + 1
                window_sum += (r_i - l_i + 1) * c_i

                while segments[j][1] < window_start:
                    lj, rj, cj = segments[j]
                    window_sum -= (rj - lj + 1) * cj
                    j += 1

                lj, rj, cj = segments[j]
                outside_part = max(0, window_start - lj) * cj

                best = max(best, window_sum - outside_part)

            return best

        # Case 1: window ends at r_i 
        case_end_at_r = bestTotal(coins)

        # Case 2: window starts at l_i
        # -> reverse (l, r) -> (-r, -l)
        mirrored = [[-r, -l, c] for l, r, c in coins]
        case_start_at_l = bestTotal(mirrored)

        return max(case_end_at_r, case_start_at_l)