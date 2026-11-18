class Solution:
    def wordSubsets(self, words1: list[str], words2: list[str]) -> list[str]:
        """
        Solution: compare frequency of target string words 2 with each str in words1
        - Build a hashmap for list of words of words2, with the frequency is the maximum freq of that character in the whole list of words of words 2
        - Compare each word in words1 with that hashmap of words2
        """
        target = Counter(words2[0])
        for word in words2:
            curr_freq = Counter(word)
            for key, value in curr_freq.items():
                if key not in target:
                    target[key] = value
                elif value > target[key]:
                    target[key] = value


        def compare_str(word_freq: str):
            for key, value in target.items():
                if key not in word_freq or value > word_freq[key]:
                    return False
            return True

        result = []
        for word in words1:
            word_freq = Counter(word)
            if compare_str(word_freq):
                result.append(word)
        
        return result
                