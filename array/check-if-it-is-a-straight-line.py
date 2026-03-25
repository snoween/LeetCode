class Solution:
    def checkStraightLine(self, coor: List[List[int]]) -> bool:
        init_dist = [coor[1][0] - coor[0][0], coor[1][1] - coor[0][1]]
        for i in range(1, len(coor)):
            if [coor[i][0] - coor[i-1][0], coor[i][1] - coor[i-1][1]] == init_dist:
                continue
            else:
                return False
        
        return True
