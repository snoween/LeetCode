class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Make a defaultdict to store tuple freq and word
        anagrams = defaultdict(list)
        # loop through input list:
        for word in strs:
            freq = [0] * 26
            # make a tuple for each word ([list freq])
            for char in word:
                freq[ord(char) - ord('a')] += 1
            # convert list freq into tuple and append the word of that tuple in dict
            anagrams[tuple(freq)].append(word)
        
        output = []
        # loop through value list in dict:
        for val in anagrams.values():
            # output append all lists of val in dict
            output.append(val)
        
        # return output
        return output
        