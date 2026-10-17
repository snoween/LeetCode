class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        flatten = []
        for row in matrix:
            flatten.extend(row)
        
        heapq.heapify(flatten)
        ans = 0
        for _ in range(k):
            ans = heapq.heappop(flatten)
        
        return ans