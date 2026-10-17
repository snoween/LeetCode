class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        freq = Counter(nums)
        result = []
        path = []

        def backtrack():
            if len(path) == len(nums):
                result.append(path[:])
                return
            
            for num in freq:
                if freq[num] == 0:
                    continue
                
                path.append(num)
                freq[num] -= 1

                backtrack()
                freq[num] += 1
                path.pop()
        
        backtrack()
        return result