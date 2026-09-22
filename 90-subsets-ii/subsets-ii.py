class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        freq = Counter(nums)
        unique_nums = list(freq.keys())
  
        result = []
        path = []

        def backtrack(idx):
            result.append(path[:])

            for i in range(idx, len(unique_nums)):
                if freq[unique_nums[i]] == 0:
                    continue
                
                path.append(unique_nums[i])
                freq[unique_nums[i]] -= 1

                backtrack(i)
                freq[unique_nums[i]] += 1
                path.pop()
        
        backtrack(0)
        return result