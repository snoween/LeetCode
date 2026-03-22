class Solution:
    def numRescueBoats(self, n: List[int], limit: int) -> int:
        n.sort()
        count = 0
        l , r = 0, len(n) - 1
        
        while l <= r:
            if n[l] + n[r] > limit:
                r -= 1
            
            else:
                r -= 1
                l += 1
            count += 1
        
        return count

