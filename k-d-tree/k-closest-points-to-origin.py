class Solution:
    def euclidean(self, x, y):
        return x*x + y*y

    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        pq = []
        for point in points:
            x, y = point
            heapq.heappush(pq, (self.euclidean(x, y), point))
        
        result = []
        for _ in range(k):
            _, coor = heapq.heappop(pq)
            result.append(coor)

        return result