class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        def find_max_len(input_char: str) -> int:
            l = 0
            init_dict = Counter()
            best_len = 0
            for r, char in enumerate(answerKey):
                init_dict[char] += 1

                while init_dict[input_char] > k:               
                    if answerKey[l] == input_char:
                        init_dict[input_char] -= 1
                    l += 1

                best_len = max(best_len, r-l+1)
            
            return best_len
            
        
        return max(find_max_len('T'), find_max_len('F'))