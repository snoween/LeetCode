class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        set_val = set(arr)
        
        if arr.count(0) >= 2:
            return True

        for num in arr:
            if (num*2) in set_val and num != 0:
                return True
            
        return False