class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        occurance = len(nums) / 3
        freq = Counter(nums)
        output = []
        
        for key, value in freq.items():
            if value > occurance:
                output.append(key)
        
        return output