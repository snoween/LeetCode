class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        positive = [num**2 for num in nums if num >= 0]
        negative = [num**2 for num in nums if num < 0][::-1]

        ans = []
        i, j = 0, 0

        while i < len(positive) and j < len(negative):
            if positive[i] <= negative[j]:
                ans.append(positive[i])
                i += 1
            else:
                ans.append(negative[j])
                j += 1
              
        ans.extend(positive[i::])
        ans.extend(negative[j::])

        return ans