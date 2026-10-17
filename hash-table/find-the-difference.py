class Solution:
    def findTheDifference(self, s: str, t: str) -> str: 
        s_dict = Counter(s)
        t_dict = Counter(t)

        # Compare keys in 2 dicts
        for key in t_dict:
            if s_dict[key] != t_dict[key]:      # if not key -> s_dict[key] = 0
                return key