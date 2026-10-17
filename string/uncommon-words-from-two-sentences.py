class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s1_words = s1.split()
        s2_words = s2.split()
        
        output = []
        comb_dict = Counter(s1_words) + Counter(s2_words)

        for key, val in comb_dict.items():
            if val == 1:
                output.append(key)
        
        return output