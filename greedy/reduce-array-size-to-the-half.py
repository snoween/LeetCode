class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        # freq_val = [1 2 3 4]
        # Remove max freq to get min num need to be removed
        # loop 1: num_del = 4 < 5
        # loop 2: num_del = 3 + 4 = 7 > 5 -> min_num_del = 2

        min_len = inf
        freq = Counter(arr)
            
        list_val = list(freq.values())
        list_val.sort()
        
        num_del = 0
        min_num_del = 0
        target = len(arr) // 2

        while num_del < target:
            num_del += list_val.pop()
            min_num_del += 1
        
        return min_num_del