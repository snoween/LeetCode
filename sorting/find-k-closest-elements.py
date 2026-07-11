class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        diff = []

        for num in arr:
            diff.append((abs(num - x), num))
        
        heapq.heapify(diff)
        k_num = []
        for i in range(k):
            k_num.append(heapq.heappop(diff)[1])
        
        return sorted(k_num)