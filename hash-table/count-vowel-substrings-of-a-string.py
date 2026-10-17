class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        vowels = set('aeiou')
        count = 0

        for i in range(len(word)):
            if word[i] not in vowels:
                continue
            count_vowel = set()
            for r in range(i, len(word)):
                if word[r] not in vowels:
                    break

                count_vowel.add(word[r])
                
                if count_vowel == vowels:
                    count += 1
                
        return count
            
            