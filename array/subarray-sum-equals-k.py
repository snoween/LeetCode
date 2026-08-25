class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_count = {0: 1}
        current_sum = 0
        count = 0

        for num in nums:
            current_sum += num
            # check if current_sum - k in dict or not
            diff = current_sum - k
            if diff in prefix_count:
                count += prefix_count[diff]
            
            # if current_sum not in dict -> default val = 0, else -> get value of that key 
            prefix_count[current_sum] = prefix_count.get(current_sum, 0) + 1
        
        return count