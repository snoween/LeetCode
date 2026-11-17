class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """
        Solution: prefix sum - count sum = target
        - Calculate the prefix sum
        - Check if prefix[left] in hashmap or not
        - Update prefix[curr_sum] = 1 to hashmap
        """
        count = 0
        curr_sum = 0
        prefix_count = {0: 1}

        for num in nums:
            curr_sum += num
            prefix_start = curr_sum - k
            if prefix_start in prefix_count:    # valid sum
                count += prefix_count[prefix_start]
            
            prefix_count[curr_sum] = prefix_count.get(curr_sum, 0) + 1
        
        return count