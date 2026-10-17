class Solution:
    def findDifferentBinaryString(self, nums: list[str]) -> str:
        set_nums = set(nums)
        n = len(nums[0])
        path = []

        def backtrack(path):
            if len(path) == n:
                return ''.join(path) not in set_nums
                    
            for num in ['0', '1']:
                path.append(num)
                if backtrack(path):
                    return ''.join(path)
                path.pop()

        return backtrack(path)