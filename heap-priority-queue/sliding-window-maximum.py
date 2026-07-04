class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = deque()
        result = []
        for i in range(k):
            # monotonic
            while queue and queue[-1] < nums[i]:
                queue.pop()
            queue.append(nums[i])

        result.append(queue[0])
        # xu ly xong cai window dau tien
        # queue[0] la so lon nhat hien tai 
        
        for i in range(k, len(nums)):
            if queue and nums[i-k] == queue[0]:
                queue.popleft()

            while queue and nums[i] > queue[-1]:
                queue.pop()  
            
            queue.append(nums[i])
            result.append(queue[0])
        
        return result