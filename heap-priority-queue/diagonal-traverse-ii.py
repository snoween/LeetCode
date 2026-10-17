class Solution:
    def findDiagonalOrder(self, nums: list[list[int]]) -> list[int]:
        groups = defaultdict(list)

        for i in range(len(nums) - 1, -1, -1):
            for j in range(len(nums[i])):
                groups[i + j].append(nums[i][j])
        
        result = []
        curr = 0
        while curr in groups:
            result.extend(groups[curr])
            curr += 1
        
        return result