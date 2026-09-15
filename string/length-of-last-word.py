class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        list_words = s.split()
        return len(list_words[-1])