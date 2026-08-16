class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        max_val = 0
        index = 0
        for i, sub_arr in enumerate(mat):
            sum_sub_arr = sum(sub_arr)
            if sum_sub_arr > max_val:
                max_val = sum_sub_arr
                index = i
    
        return [index, max_val]