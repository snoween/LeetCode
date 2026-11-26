class Solution:
    def longestPalindrome(self, s: str) -> int:
        """
        Solution: counter
        - Count the frequency of all characters in the list
        - If the frequency of a character is 3 -> we can use 2 and remove 1
        -> count how many characters have odd freq -> input length - odd_count
        - But 1 character can be odd value -> final ans is: 
        longest len = input length - odd_count + 1
        - In case have 0 characters have odd freq -> return input length
        """
        freq = Counter(s)
        odd_count = 0
        input_length = len(s)

        for value in freq.values():
            odd_count += int(value % 2 != 0)
        
        if odd_count == 0:     # in case all characters have even freqs -> longest = input len
            return input_length
            
        return input_length - odd_count + 1     # plus 1 because 1 character can have odd freq