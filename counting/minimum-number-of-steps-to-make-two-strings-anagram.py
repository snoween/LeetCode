class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s_dict = Counter(s)
        t_dict = Counter(t)
        
        count_chars = 0

        for key, value in s_dict.items():
            missing_chars = value - t_dict[key]

            # Check num of missing chars
            count_chars += max(0, missing_chars)
        
        return count_chars