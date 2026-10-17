class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

        letter = {chr(ord('a') + i): morse[i] for i in range(26)}
        
        set_code = set()
        for word in words:
            code = []
            for char in word:
                code.append(letter[char])
            set_code.add(''.join(code))
        
        return len(set_code)
