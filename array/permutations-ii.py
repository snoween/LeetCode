class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        result = []
        freq = Counter(nums)
        list_nums = []

        def backtrack():
            if len(list_nums) == len(nums):
                result.append(list_nums[:])
                return
            
            for num in freq:
                if freq[num] == 0:
                    continue
                
                list_nums.append(num)
                freq[num] -= 1
                backtrack()
                freq[num] += 1
                list_nums.pop()
        
        backtrack()
        return result