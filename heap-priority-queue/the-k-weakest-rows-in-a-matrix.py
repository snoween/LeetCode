class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        result = []
        row_sum = []

        for i in range(len(mat)):
            current_sum = 0
            for j in range(len(mat[0])):
                current_sum += mat[i][j]
            row_sum.append((current_sum, i))
        
        heapq.heapify(row_sum)
        for i in range(k):
            result.append(heapq.heappop(row_sum)[1])
        
        return result