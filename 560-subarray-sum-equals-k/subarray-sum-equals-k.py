class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """
        Solution: prefix sum - count sum = target
        - Calculate the prefix sum
        - Check if prefix[left] in hashmap or not
        - Update prefix[curr_sum] = 1 to hashmap
        """
        n = len(nums)
        count = 0
        prefix_count = {0: 1}
        curr_sum = 0
        for num in nums:
            curr_sum += num
            # check if prefix_start in hashmap
            prefix_start = curr_sum - k
            if prefix_start in prefix_count:
                count += prefix_count[prefix_start]
            
            # add curr_sum to hashmap for future check
            prefix_count[curr_sum] = prefix_count.get(curr_sum, 0) + 1
        
        return count
        
