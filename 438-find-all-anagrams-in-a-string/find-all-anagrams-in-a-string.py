class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        len_s, len_p = len(s), len(p)
        target = Counter(p)
        curr_arr = Counter(s[:len_p])
        output = [0] if curr_arr == target else []

        left = 0
        for right in range(len_p, len_s):
            curr_arr[s[right]] += 1
            curr_arr[s[left]] -= 1

            if curr_arr == target:
                output.append(left+1)
            
            left += 1
        
        return output