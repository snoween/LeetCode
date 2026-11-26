class Solution:
    def distributeCandies(self, candyType: list[int]) -> int:
        """
        - If has 6 types of candies [1 2 3 4 5 6]-> limit is 3 -> return 3
        - If has 2 types of candies [1 1 1 1 2 2 2 2]-> limit is 4 -> return 2
        """
        types = len(set(candyType))
        limit = len(candyType) // 2

        if types >= limit:
            return limit
        
        return types