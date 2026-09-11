class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        """
        Time comp: O(N + klogN)
        Space comp: O(N)
        """
        heap = [(num, i) for i, num in enumerate(nums)]
        heapq.heapify(heap)

        for _ in range(k):
            num, idx = heapq.heappop(heap)
            num *= multiplier
            heapq.heappush(heap, (num, idx))
        
        # Put digit with init index after operations
        ans = [0] * len(nums)
        for digit, index in heap:
            ans[index] = digit
        
        return ans