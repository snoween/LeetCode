class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums_neg = [num * -1 for num in nums]
        heapq.heapify(nums_neg)
        element_1 = heapq.heappop(nums_neg) + 1
        element_2 = heapq.heappop(nums_neg) + 1
        return element_1 * element_2
