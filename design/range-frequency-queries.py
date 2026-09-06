class RangeFreqQuery:

    def __init__(self, arr: List[int]):
        self.val_idx = defaultdict(list)

        for i, num in enumerate(arr):
            self.val_idx[num].append(i)

    def query(self, left: int, right: int, value: int) -> int:
        if value not in self.val_idx:
            return 0
        
        idx = self.val_idx[value]

        def find_left(lst, target):
            low, high = 0, len(lst)

            while low < high:
                middle = low + (high - low) // 2
                if lst[middle] < target:
                    low = middle + 1
                else:
                    high = middle
            
            return low
        
        def find_right(lst, target):
            low, high = 0, len(lst)

            while low < high:
                middle = low + (high - low) // 2
                if lst[middle] <= target:
                    low = middle + 1
                else:
                    high = middle
            
            return low
        
        l = find_left(idx, left)
        r = find_right(idx, right)

        return r - l



# Your RangeFreqQuery object will be instantiated and called as such:
# obj = RangeFreqQuery(arr)
# param_1 = obj.query(left,right,value)