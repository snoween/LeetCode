class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        li_s = list(s)
       
        for i in range(0, len(li_s), 2*k):
            l, r = i, i + (k - 1)

            while l < r:
                li_s[l], li_s[r] = li_s[r], li_s[l]
                l += 1
                r -= 1
            
        return ''.join(li_s)
        

