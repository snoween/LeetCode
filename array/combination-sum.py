class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        result = []
        path = []

        def backtrack(total, index):
            if total >= target:
                if total == target:
                    result.append(path[:])
                return
            
            for i in range(index, len(candidates)):
                path.append(candidates[i])
                backtrack(total + candidates[i], i)
                path.pop()
        
        backtrack(0, 0)
        return result