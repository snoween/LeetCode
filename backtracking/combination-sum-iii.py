class Solution:
    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        result = []
        path = []

        def backtrack(start, total):
            if len(path) == k and total == n:
                result.append(path[:])
                return
            
            for i in range(start, 10):
                path.append(i)
                backtrack(i + 1, total + i)
                path.pop()
        
        backtrack(1, 0)
        return result