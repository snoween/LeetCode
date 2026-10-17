class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count_t = Counter(t)
        curr_arr = Counter()

        output_len = inf
        output_index = []
        curr_len = 0

        left = 0
        for right, char in enumerate(s):
            curr_arr[char] += 1

            while (curr_arr & count_t) == count_t:
                curr_len = right-left+1
                output_len = min(output_len, curr_len)
                
                if curr_len == output_len:   # Update output_index if output_len is changed
                    output_index = [left, left+output_len]

                curr_arr[s[left]] -= 1
                left += 1
    
        if output_len == inf:
            return ""
        
        return s[output_index[0]: output_index[1]]