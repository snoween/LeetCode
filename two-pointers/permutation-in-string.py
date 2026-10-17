class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l1, l2 = len(s1), len(s2)
        target = Counter(s1)
        curr_arr = Counter(s2[:l1])

        if curr_arr == target:
            return True
        
        left = 0
        for right in range(l1, l2):
            curr_arr[s2[right]] += 1
            curr_arr[s2[left]] -= 1
            
            if curr_arr == target:
                return True
            
            left += 1
        
        return False