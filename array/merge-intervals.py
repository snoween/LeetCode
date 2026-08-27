class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        heap_intervals = []
        start_end = defaultdict(int)

        for interval in intervals:
            heapq.heappush(heap_intervals, tuple(interval))
        
        curr_start, curr_end = heapq.heappop(heap_intervals)
        start_end[curr_start] = curr_end
        while heap_intervals:
            start, end = heapq.heappop(heap_intervals)
            
            if start <= curr_end and end >= curr_end:
                start_end[curr_start] = end
            elif start <= curr_end and end <= curr_end:
                continue
            else:
                start_end[start] = end
                curr_start = start
                curr_end = end
        
        
        results = []
        for key, val in start_end.items():
            results.append([key, val])
        
        return results
