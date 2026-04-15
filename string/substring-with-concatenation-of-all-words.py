class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        set_words = Counter(words)
        output = []

        # Get len of curr_arr
        m = len(words[0])
        n = m * len(words)
        curr_arr = s[:n]

        # Chunk the curr_arr
        chunks = Counter([curr_arr[i: i+m] for i in range(0, n, m)])
        if chunks == set_words:
            output.append(0)
        
        # Update output in case Counter(chunks) = set_words
        for r in range(n, len(s)):
            curr_arr = curr_arr[1:] + s[r]
            chunks = Counter([curr_arr[i: i+m] for i in range(0, n, m)])
       
            if chunks == set_words:
                output.append(r - n + 1)
        
        return output