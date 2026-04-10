class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        init_dict = Counter()
        char_less = ''
        l = 0
        best_len_T = 0
        best_len_F = 0
        for r, char in enumerate(answerKey):
            init_dict[char] += 1

            while init_dict['T'] > k:               
                if answerKey[l] == 'T':
                    init_dict['T'] -= 1
                l += 1

            best_len_T = max(best_len_T, r-l+1)
        
        l = 0
        init_dict_F = Counter()
        for r, char in enumerate(answerKey):
            init_dict_F[char] += 1

            while init_dict_F['F'] > k:               
                if answerKey[l] == 'F':
                    init_dict_F['F'] -= 1
                l += 1

            best_len_F = max(best_len_F, r-l+1)
            
        return max(best_len_T, best_len_F)