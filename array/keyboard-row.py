class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        keyboard = [set("qwertyuiop"), set("asdfghjkl"), set("zxcvbnm")]
        results = []

        for word in words:
            set_word = set(word.lower())
            for row in keyboard:
                if set_word.issubset(row):     # Check if subset
                    results.append(word)
                    break
                    
        return results
