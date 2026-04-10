class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        def find_max_len(input_char: str) -> int:
            init_dict = Counter()
            best_len = 0
            
            l = 0
            for r, char in enumerate(s):
                init_dict[char] += 1

                while init_dict[input_char] > k:               
                    if s[l] == input_char:
                        init_dict[input_char] -= 1
                    l += 1

                best_len = max(best_len, r-l+1)
            
            return best_len
        
        set_s = set(s)
        ans = 0

        for char in set_s:
            len_char = find_max_len(char)
            ans = max(ans, len_char)

        return ans if len(set_s) > 1 else len(s)