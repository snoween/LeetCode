class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # tao dict s[i]: t[i]
        s_to_t = {}

        # loop qua 2 dayx s, t
        for i, char in enumerate(s):
            
            # check if t[i] != dict[s[i]] -> Fals
            if char not in s_to_t:
                s_to_t[char] = t[i]
            
            else:
                if s_to_t[char] != t[i]:
                    return False

        
        t_to_s = {}

        # loop qua 2 dayx s, t
        for i, char in enumerate(t):
            
            # check if t[i] != dict[s[i]] -> Fals
            if char not in t_to_s:
                t_to_s[char] = s[i]
            
            else:
                if t_to_s[char] != s[i]:
                    return False
        
        return True