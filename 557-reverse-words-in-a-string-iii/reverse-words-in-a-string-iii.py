class Solution:
    def reverseWords(self, s: str) -> str:
        # pattern: 2 pointers
        # convert str s to list
        list_words = s.split(" ")

        def reverse_word(word):
            list_word = list(word)
            left = 0
            right = len(list_word) - 1
  
            # while left < right
            while left < right:
                # swap left, right
                list_word[left], list_word[right] = list_word[right], list_word[left]
                # left + 1, right - 1
                left += 1
                right -= 1

            return ''.join(list_word)

        output = []
        # loop curr_idx, char through list s
        for word in list_words:
            output.append(reverse_word(word))
                
        
        # return join list
        return ' '.join(output)
            