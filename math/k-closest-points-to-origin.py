class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def euclidean(points):
            return (points[0] ** 2 + points[1] ** 2) 

        dis_heap = []

        for point in points:
            dis_heap.append((euclidean(point), point))     

        heapq.heapify(dis_heap)
        output = []
        for i in range(k):
            output.append(heapq.heappop(dis_heap)[1])
        
        return output