class Solution:
    def findRestaurant(self, list1: list[str], list2: list[str]) -> list[str]:
        freq1 = {word: i for i, word in enumerate(list1)}
        freq2 = {word: i for i, word in enumerate(list2)}

        valid_word = []
        min_sum = float('inf')

        for key, value in freq1.items():
            if key in freq2:
                curr_sum = value + freq2[key]
                if curr_sum <= min_sum:
                    min_sum = curr_sum
                    valid_word.append((curr_sum, key))
        
        result = []
        for total, word in valid_word:
            if total == min_sum:
                result.append(word)

        print(result)
        return result