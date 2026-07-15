class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        def FindMaxMinHeap(arr):
            max_heap = []
            min_heap = []

            for num in arr:
                heapq.heappush(max_heap, -num)
                max_num = heapq.heappop(max_heap)
                heapq.heappush(min_heap, -max_num)

                if len(min_heap) > len(max_heap):
                    min_num = heapq.heappop(min_heap)
                    heapq.heappush(max_heap, -min_num)
            
            return (max_heap, min_heap)
        
        def CalculateMedian(max_heap, min_heap):
            if len(max_heap) == len(min_heap):
                return ((min_heap[0] - max_heap[0]) / 2)
            else:
                return float(-max_heap[0])
        
        def helper(arr):
            max_heap, min_heap = FindMaxMinHeap(arr)
            return CalculateMedian(max_heap, min_heap)

        ###########################
        result = []
        curr_queue = deque()

        for i in range(k):
            curr_queue.append(nums[i])
        
        result.append(helper(curr_queue))

        for i in range(k, len(nums)):
            curr_queue.popleft()
            curr_queue.append(nums[i])
            result.append(helper(curr_queue))
        
        return result
