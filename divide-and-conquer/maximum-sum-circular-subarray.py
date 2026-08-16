class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)

        # Double the length of array nums -> to get circular array
        nums_double = nums + nums

        # calculate prefix sum of doubly array
        prefix_sum = [0] * (2 * n + 1)
        for i in range(2 * n):
            prefix_sum[i + 1] = prefix_sum[i] + nums_double[i]
        
        print(prefix_sum)
        # set init max sum = first ele of 'nums'
        max_sum = nums[0]
        # set init deque to store num of prefix sum
        queue = deque()
        queue.append(0)

        for i in range(1, 2 * n + 1):
            # if out of bound -> remove
            if queue[0] < (i - n):
                queue.popleft()
            
            # update max sum 
            max_sum = max(max_sum, prefix_sum[i] - prefix_sum[queue[0]])

            # update queue
            while queue and prefix_sum[queue[-1]] >= prefix_sum[i]:
                queue.pop()
            queue.append(i)
        
        return max_sum

        
