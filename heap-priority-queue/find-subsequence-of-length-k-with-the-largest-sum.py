class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        # Max heap -> Take sum of the first k numbers
        nums_minus = []
        for i, num in enumerate(nums):
            nums_minus.append([-num, i])
        heapq.heapify(nums_minus)
        result = []

        for i in range(k):
            index = nums_minus[i][1]
            result.append([-heapq.heappop(nums_minus[i]), index])
        
        return [item[0] for item in sorted(result, key=lambda x: x[1])]