class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        result = []
        def backtrack(start_idx, total, list_num):
            if total > target:
                return result
            
            if total == target:
                result.append(list(list_num))
                return result
            
            for i in range(start_idx, len(candidates)):
                list_num.append(candidates[i])
                backtrack(i, total + candidates[i], list_num)
            
                list_num.pop()
        
        backtrack(0, 0, [])
        return result