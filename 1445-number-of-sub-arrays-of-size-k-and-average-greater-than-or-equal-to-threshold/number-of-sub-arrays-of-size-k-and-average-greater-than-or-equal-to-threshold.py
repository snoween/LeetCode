class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        current_sum = sum(arr[:k])
        count = 1 if (current_sum) / k >= threshold else 0

        for r in range(k, len(arr)):
            current_sum = current_sum + arr[r] - arr[r-k]
            
            if (current_sum) / k >= threshold:
                print(current_sum / k)
                count += 1
        
        return count