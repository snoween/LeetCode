class Solution:
    def findLucky(self, arr: List[int]) -> int:
        arr_dict = Counter(arr)

        max_key = -1
        for key, val in arr_dict.items():
            if key == val:
                max_key = max(max_key, key)
        
        return max_key
