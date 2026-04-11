class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        curr_arr = s[:10]
        seen = set()
        ans = set()
        
        seen.add(curr_arr)
        for r in range(10, len(s)):
            curr_arr = curr_arr[1:] + s[r]
            if curr_arr in seen and curr_arr not in ans:
                ans.add(curr_arr)
            seen.add(curr_arr)
        
        return list(ans)