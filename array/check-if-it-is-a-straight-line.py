class Solution:
    def checkStraightLine(self, coor: List[List[int]]) -> bool:
        sorted_coor = sorted(coor, key=lambda x: (x[0], x[1]))

        init_dist = [sorted_coor[1][0] - sorted_coor[0][0], sorted_coor[1][1] - sorted_coor[0][1]]

        for i in range(1, len(coor)):
            dist = [sorted_coor[i][0] - sorted_coor[i-1][0], sorted_coor[i][1] - sorted_coor[i-1][1]]
            if dist == init_dist:
                continue
            else:
                return False
        
        return True
