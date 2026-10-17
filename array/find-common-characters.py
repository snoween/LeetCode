class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        # Get init dict using the first word in list
        init_dict = Counter(words[0])
        output = []
        
        for word in words:
            word_dict = Counter(word)

            for key, val in init_dict.items():
                # Get the minimum value of that letter
                if key in word_dict:
                    init_dict[key] = min(word_dict[key], val)   
                
                # If letter not in other words -> assign to 0
                else:
                    init_dict[key] = 0
        
        for key, val in init_dict.items():
            output.extend(list(key)*val)
        
        return output
