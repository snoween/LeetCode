class Solution:
    def checkStraightLine(self, coor: List[List[int]]) -> bool:
        sorted_coor = sorted(coor, key=lambda x: (x[0], x[1]))

        # Check if x-line
        if sorted_coor[1][0] == sorted_coor[0][0]:
            for i in range(2, len(sorted_coor)):
                if sorted_coor[i][0] == sorted_coor[i-1][0]:
                    continue
                else:
                    return False
        
        # Check if y-line
        elif sorted_coor[1][1] == sorted_coor[0][1]:
            for i in range(2, len(sorted_coor)):
                if sorted_coor[i][1] == sorted_coor[i-1][1]:
                    continue
                else:
                    return False
        
        # Other circumstances
        else:
            coef_a = (coor[1][1] - coor[0][1]) / (coor[1][0] - coor[0][0])  
            coef_b = coor[1][1] - coef_a * coor[1][0]

            for i in range(1, len(coor)):
                func = coef_a * coor[i][0] + coef_b
                if func == coor[i][1]:
                    continue
                else:
                    return False
        
        return True
