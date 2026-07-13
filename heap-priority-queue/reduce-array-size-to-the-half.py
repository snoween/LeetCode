class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        min_len = inf
        freq = Counter(arr)
        if len(freq) == 1:
            return 1
        list_val = list(freq.values())
        list_val.sort()
        
        left = 0
        curr_sum = 0
        for right, num in enumerate(list_val):
            curr_sum += num
            while left < right and curr_sum >= len(list_val) // 2:
                min_len = min(min_len, right - left + 1)
                curr_sum -= list_val[left]
                left += 1
        
        return min_len