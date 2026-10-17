class Solution:
    def sumOfMultiples(self, n: int) -> int:
        li_n = [_ for _ in range(1, n+1)]
        total = 0
        l, r = 0, n-1

        while l <= r:
            if li_n[l] % 3 == 0 or li_n[l] % 5 == 0 or li_n[l] % 7 == 0:
                total += li_n[l]

            if li_n[r] % 3 == 0 or li_n[r] % 5 == 0 or li_n[r] % 7 == 0:
                if l != r:      # Avoid same mid point
                    total += li_n[r]
            
            l += 1
            r -= 1
        
        return total