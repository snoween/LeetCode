class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        target = Counter('abc')
        l = 0
        count = 0
        curr_dict = Counter()

        for r, char in enumerate(s):
            curr_dict[char] += 1

            while curr_dict['a'] >= 1 and curr_dict['b'] >= 1 and curr_dict['c'] >= 1:
                curr_dict[s[l]] -= 1
                count += (len(s) - r)
                l += 1
            
        return count