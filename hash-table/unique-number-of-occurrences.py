class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        
        # dict to get val: count
        freq = {}
        for num in arr:
            if num not in freq:
                freq[num] = 0
            freq[num] += 1
        
        # set to check unique of values in dict
        s_nums = set()

        for num in freq.values():
            if num in s_nums:
                return False
                
            s_nums.add(num)

        return True