class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        result = []
        path = []

        def backtrack(num):
            if len(path) == k:
                result.append(path[:])
                return
            
            if num > n:
                return
            
            path.append(num)
            backtrack(num + 1)

            path.pop()
            backtrack(num + 1)
        
        backtrack(1)
        return result