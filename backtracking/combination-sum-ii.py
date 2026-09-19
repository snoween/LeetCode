class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort()
        result = []
        list_num = []

        def backtrack(start_idx, total):
            if total >= target:
                if total == target:
                    result.append(list_num[:])
                return result
            
            for i in range(start_idx, len(candidates)):
                # Avoid repeating
                if i > start_idx and candidates[i] == candidates[i - 1]:
                    continue
                
                list_num.append(candidates[i])
                backtrack(i + 1, total + candidates[i])
                list_num.pop()
        
        backtrack(0, 0)
        return result