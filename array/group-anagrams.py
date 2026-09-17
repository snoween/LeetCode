class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        """
        Method: use tuple of freq of letters as keys, values are words that have the 
        same number of letters
        """
        freq = defaultdict(list)

        for word in strs:
            count = [0] * 26
            for char in word:
                idx = ord(char) - ord('a')
                count[idx] += 1
            freq[tuple(count)].append(word)
        
        result = []
        for list_words in freq.values():
            result.append(list_words)
        
        return result
            