class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = re.findall(r'\w+', paragraph.lower())
        set_banned = set(banned)
        freq = defaultdict(int)

        for word in words:
            if word not in set_banned:
                freq[word] += 1

        return max(freq, key=freq.get)   