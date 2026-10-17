class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        freq = Counter(candidates)
        unique_nums = list(freq.keys())
        result = []
        path = []

        def backtrack(start_idx, total):
            if total >= target:
                if total == target:
                    result.append(path[:])
                return
            
            for i in range(start_idx, len(unique_nums)):
                if freq[unique_nums[i]] == 0:
                    continue
                path.append(unique_nums[i])
                freq[unique_nums[i]] -= 1
                # backtrack from i to make sure use all unique num freq
                backtrack(i, total + unique_nums[i])
                # Undo part
                freq[unique_nums[i]] += 1
                path.pop()
        
        backtrack(0, 0)
        return result