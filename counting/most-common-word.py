class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = paragraph.split()
        set_banned = set(banned)
        freq = defaultdict(int)

        for word in words:
            cleaned_word = word.lower().strip("!?',;.")
            if cleaned_word and cleaned_word not in set_banned:
                freq[cleaned_word] += 1

        return max(freq, key=freq.get)

        