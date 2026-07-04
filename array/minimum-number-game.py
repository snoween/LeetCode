class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        heapq.heapify(nums)
        result = []

        for i in range(0, len(nums), 2):
            element1 = heapq.heappop(nums)
            element2 = heapq.heappop(nums)
            result.append(element2)
            result.append(element1)
        
        return result