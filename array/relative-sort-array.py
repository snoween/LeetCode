class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr1_dict = Counter(arr1)
        res = []

        # Get the elements in order based on arr2
        for ele in arr2:
            res.extend([ele] * arr1_dict[ele])

        # Get the remaining sorted-elements
        arr1_sorted = sorted(arr1_dict.keys())
        for ele in arr1_sorted:
            if ele not in arr2:
                res.extend([ele] * arr1_dict[ele])
        
        return res