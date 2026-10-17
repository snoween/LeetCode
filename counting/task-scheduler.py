class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        freq = Counter(tasks).values()
        pq = [-num for num in freq]
        heapq.heapify(pq)

        queue = deque()
        time = 0

        while pq or queue:
            time += 1

            if pq:
                curr = heapq.heappop(pq) + 1
                if curr != 0:
                    queue.append([curr, time + n])
            
            # check first task in queue if available
            if queue and queue[0][1] == time:
                heapq.heappush(pq, queue.popleft()[0])
        
        return time

