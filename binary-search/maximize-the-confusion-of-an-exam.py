class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        init_dict = Counter(answerKey)
        char_less = 'T' if init_dict['T'] == min(init_dict.values()) else 'F'
        count = 0
        l = 0
        best_len = 0
        for r, char in enumerate(answerKey):
            if char == char_less:
                count += 1
            
            while count > k:
                if answerKey[l] == char_less:
                    count -= 1
                l += 1

            best_len = max(best_len, r-l+1)
        return best_len
            
