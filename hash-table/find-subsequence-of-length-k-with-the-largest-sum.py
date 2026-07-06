class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        # Max heap -> Take sum of the first k numbers
        nums_minus = [-num for num in nums]
        heapq.heapify(nums_minus)
        result = []

        for i in range(k):
            result.append(-heapq.heappop(nums_minus))
        
        left, right = 0, len(result) - 1
        while left < right:
            result[left], result[right] = result[right], result[left]
            left += 1
            right -= 1
        
        return result