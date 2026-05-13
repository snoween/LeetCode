class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        curr_sum = 0
        for i in range(k):
            curr_sum += arr[i]
        count = int(curr_sum >= threshold * k)
        # count = 1 if avg curr_sum >= threshold else 0

        # for loop (k, len(nums))
        for i in range(k, len(arr)):
            # Update curr_sum: + right ele, - left ele
            curr_sum = curr_sum + arr[i] - arr[i-k]
            # Update count
            count += int(curr_sum >= threshold * k)
        
        return count