class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        # Init param int
        currSum = 0
        subarrays = 0
        prefixSum = defaultdict(int, {currSum: 1})  # store freq of currSum

        for r, num in enumerate(nums):
            currSum += (num % 2)    # prefix sum of nums[i] 
            
            if currSum - k in prefixSum:    # currSum - k: left pointer
                subarrays += prefixSum[currSum -k]  # valid array = arr[left:right] = prefixSum[currSum - k]
            
            prefixSum[currSum] += 1     # update freq of right pointer
            
        return subarrays   