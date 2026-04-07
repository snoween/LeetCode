class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        s_counter = Counter(s)
        l = 0
        if len(s_counter.keys()) < 2:
            return max(s_counter.values())

        min_char = min(s_counter.values())
        char = ''
        for key in s_counter.keys():
            if s_counter[key] == min_char:
                char = key
        count = 0
        max_char = 0

        for r in range(len(s)):
            if s[r] == char:
                count += 1
            
            while count > k:
                if s[l] == char:
                    count -= 1
                l += 1
            
            max_char = max(max_char, r-l+1)
        
        return max_char