class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        max_len = 0
        max_freq = 0
        freq = defaultdict(int)
        l = 0

        for r, char in enumerate(answerKey):
            freq[char] += 1
            max_freq = max(max_freq, freq[char])

            while (r-l+1) - max_freq > k:
                freq[answerKey[l]] -= 1
                l += 1
            
            max_len = max(max_len, r-l+1)
        
        return max_len