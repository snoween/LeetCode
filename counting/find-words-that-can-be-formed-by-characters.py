class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        chars_dict = Counter(chars)
        count_len = 0

        for word in words:
            word_dict = Counter(word)
            if word_dict < chars_dict:      # Check if subset
                count_len += len(word)
        
        return count_len