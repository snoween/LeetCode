class Solution:
    def reverseWords(self, s: str) -> str:
        li_words = [word for word in s.split()]
        l, r = 0, len(li_words) - 1
        
        while l < r:
            li_words[l], li_words[r] = li_words[r], li_words[l]
            l += 1
            r -= 1

        return " ".join(li_words)