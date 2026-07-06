class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        # Max heap -> Take sum of the first k numbers
        nums_minus = []
        for i, num in enumerate(nums):
            nums_minus.append([num, i])
        heapq.heapify(nums_minus)

        while len(nums_minus) > k:
            heapq.heappop(nums_minus)
           
        return [item[0] for item in sorted(nums_minus, key=lambda x: x[1])]