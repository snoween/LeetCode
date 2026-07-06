class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums_minus = [-num for num in nums]
        heapq.heapify(nums_minus)
        result = 0

        while k > 0:
            result = -heapq.heappop(nums_minus)
            k -= 1
        
        return result