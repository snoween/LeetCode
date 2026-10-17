class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        word_dict = Counter('balloon')
        text_dict = Counter(text)
        sub_dict = defaultdict(lambda: 0)

        # Get balloon dict from text_dict
        for key in word_dict.keys():
            sub_dict[key] = text_dict[key]
        
        # Get the lowest of num words that can be created
        min_words = []
        for key in sub_dict.keys():
            char_count = sub_dict[key] // word_dict[key]
            min_words.append(char_count)

        return min(min_words)