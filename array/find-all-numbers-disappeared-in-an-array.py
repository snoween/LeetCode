class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        seen = [False] * (n+1)
        output = []

        for num in nums:
            seen[num] = True
        
        for i in range(1, n+1):
            if not seen[i]:
                output.append(i)
        
        return output