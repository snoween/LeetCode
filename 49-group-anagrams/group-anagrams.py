class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Make a dict to store signature of word as key, word as val
        group_ana = defaultdict(list)
        # loop through strs
        for word in strs:
            # make a list 0s to store freq of each char
            freq = [0] * 26
            # loop through word
            for char in word:
                # get the index of that word by ord(char) - ord('a')
                index = ord(char) - ord('a')
                # update freq based on index
                freq[index] += 1
            
            # update dict with key: tuple of the list freq, val: word
            group_ana[tuple(freq)].append(word)
        
        output = []
        # loop through all values in dict
        for val in group_ana.values():
            # append those val lists to output
            output.append(val)

        # return output 
        return output