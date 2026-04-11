class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        curr_arr = s[:10]
        seen = []
        ans = []
        
        seen.append(curr_arr)
        for r in range(10, len(s)):
            curr_arr = curr_arr[1:] + s[r]
            if curr_arr in seen and curr_arr not in ans:
                ans.append(curr_arr)
            
            seen.append(curr_arr)
        
        return ans