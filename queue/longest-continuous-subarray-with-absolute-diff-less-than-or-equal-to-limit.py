class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        queue_max = deque()
        queue_min = deque()

        max_length = 0
        left = 0

        for i, num in enumerate(nums):
            while queue_max and num > queue_max[0]:
                queue_max.pop()
            queue_max.append(num)

            while queue_min and num < queue_min[0]:
                queue_min.pop()
            queue_min.append(num)

            while queue_max and queue_min and abs(queue_max[0] - queue_min[0]) > limit:
                if queue_max and queue_max[0] == nums[left]:
                    queue_max.popleft()
                if queue_min and queue_min[0] == nums[left]:
                    queue_min.popleft()
                left += 1

            max_length = max(max_length, i - left + 1)
        
        return max_length