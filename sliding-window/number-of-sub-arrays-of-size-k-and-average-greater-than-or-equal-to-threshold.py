class Solution:
    def numOfSubarrays(self, arr: list[int], k: int, threshold: int) -> int:
        """
        Solution: Sliding window with fixed size k
        Calculate avg of subarray size k -> compare with threshold
        """
        currentSum = 0
        for i in range(k):
            currentSum += arr[i]
        
        count = int((currentSum / k) >= threshold)

        for j in range(k, len(arr)):
            currentSum = currentSum + arr[j] - arr[j - k]
            count += int((currentSum / k) >= threshold)
        
        return count