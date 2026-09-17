class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        """
        Method: use tuple of freq of letters as keys, values are words that have the 
        same number of letters
        """
        alphabet = {chr(i): i - ord('a') for i in range(ord('a'), ord('z') + 1)}
        freq = defaultdict(list)

        for word in strs:
            count = [0] * 26
            for char in word:
                count[alphabet[char]] += 1
            freq[tuple(count)].append(word)
        
        result = []
        for list_words in freq.values():
            result.append(list_words)
        
        return result
            