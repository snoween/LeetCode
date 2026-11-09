class Solution:
    def distributeCandies(self, candyType: list[int]) -> int:
        types = len(set(candyType))
        limit = len(candyType) // 2

        if types >= limit:
            return limit
        
        return types