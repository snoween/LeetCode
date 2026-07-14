class Solution:
    def minSetSize(self, arr: List[int]) -> int:
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