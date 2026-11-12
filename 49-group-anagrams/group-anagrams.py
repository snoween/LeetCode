class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        """
        - Need to group those words with same frequency of characters in a word
        - Dictionary to group and look up, key is a tuple with length = 26
        - tuple will present the frequency of characters in a word
        """
        freq = defaultdict(list)

        for word in strs:
            key = [0] * 26
            for char in word:
                idx = ord(char) - ord('a')
                key[idx] += 1
            
            freq[tuple(key)].append(word)
        
        return [lst_word for lst_word in freq.values()]