class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        m, n = len(s), len(p)
        curr_win = s[:n]
        target_dict = Counter(p)
        output = [0] if Counter(curr_win) == target_dict else []

        for i in range(1, m):
            curr_win = s[i:i+n]
            if Counter(curr_win) == target_dict:
                output.append(i)
        
        return output  