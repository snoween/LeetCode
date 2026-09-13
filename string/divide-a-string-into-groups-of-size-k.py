class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        remaining = len(s) % k

        if remaining != 0:
            s += fill * (k - remaining)

        ans = []
        for i in range(0, len(s), k):
            ans.append(''.join(s[i: i+k]))
        
        return ans