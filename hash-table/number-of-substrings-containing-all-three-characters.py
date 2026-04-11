class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        target = Counter('abc')
        l = 0
        count = 0
        curr_dict = Counter()

        for r, char in enumerate(s):
            curr_dict[char] += 1

            while len(curr_dict) == 3:
                curr_dict[s[l]] -= 1
                if curr_dict[s[l]] == 0:
                    del curr_dict[s[l]]
                count += (len(s) - r)
                l += 1
            
        return count