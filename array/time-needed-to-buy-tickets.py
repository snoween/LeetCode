class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        queue = deque(range(len(tickets)))
        time = 0

        while queue:
            curr = queue.popleft()

            # buy 1 ticket takes 1 sec
            tickets[curr] -= 1
            time += 1

            # if k-th person done -> return time
            if curr == k and tickets[curr] == 0:
                return time
            
            # back to queue
            if tickets[curr] > 0:
                queue.append(curr)
        
        return time