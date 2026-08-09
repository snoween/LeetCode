class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        # make a set of dictionary
        root_set = set(dictionary)

        # func to check prefix of word -> search in set
        def get_root(word):
            # loop through len word
            for i in range(1, len(word) + 1):
                # increase prefix through loop: r -> ra -> rat -> ...
                prefix = word[:i]
                # if in root set
                if prefix in root_set:
                    # return prefix
                    return prefix
            
            # if not in root set -> return word
            return word
        
        # split words sentence
        list_words = sentence.split()
        # result = []
        result = []
        # loop through words split
        for word in list_words:
            # call func on word -> append to result
            result.append(get_root(word))
        
        # return join result
        return ' '.join(result)
            