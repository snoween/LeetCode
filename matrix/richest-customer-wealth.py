class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        richest = -inf
        for row in accounts:
            richest = max(richest, (list(accumulate(row)))[-1])
        
        return richest