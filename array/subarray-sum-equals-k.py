class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """
        Solution: Prefix sum - hashmap
        - Subarray might have different lengths
        - The total of a subarray -> prefix sum: prefix[right] - prefix[left - 1] = k
        - prefix[right] = sum(subarray)
        -> save prefix[left - 1] in hashmap to find
        - if found prefix[left - 1] in hashmap -> have a valid sum = k -> update count
        """
        prefix_count = {0: 1}   # base case: sum = 0 appears 1 time
        count = 0
        curr_sum = 0

        for num in nums:
            curr_sum += num
            prefix_left = curr_sum - k

            if prefix_left in prefix_count:
                count += prefix_count[prefix_left]
            
            prefix_count[curr_sum] = prefix_count.get(curr_sum, 0) + 1
        
        return count