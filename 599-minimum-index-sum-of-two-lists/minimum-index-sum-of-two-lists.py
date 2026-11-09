class Solution:
    def findRestaurant(self, list1: list[str], list2: list[str]) -> list[str]:
        word_idx = {word: i for i, word in enumerate(list1)}

        result = []
        min_sum = float('inf')

        for i, word in enumerate(list2):
            if word in word_idx:
                curr_sum = i + word_idx[word]

                # if found smaller sum -> reset the list of result
                if curr_sum < min_sum:
                    min_sum = curr_sum
                    result = [word]
                elif curr_sum == min_sum:
                    result.append(word)
                    
        return result