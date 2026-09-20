class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        result = []
        path = []

        def backtrack(start, total):
            if total >= target:
                if total == target:
                    result.append(path[:])
                return
            
            for i in range(start, len(candidates)):
                path.append(candidates[i])
                backtrack(i, total + candidates[i])
                path.pop()
        
        backtrack(0, 0)
        return result