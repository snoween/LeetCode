class Solution:
    def minCostToMoveChips(self, position: list[int]) -> int:
        even_move = 0
        odd_move = 0

        for pos in position:
            if pos % 2 == 0:
                even_move += 1
            else:
                odd_move += 1
        
        return min(even_move, odd_move)