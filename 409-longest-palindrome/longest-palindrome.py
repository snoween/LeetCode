class Solution:
    def longestPalindrome(self, s: str) -> int:
        """
        Solution: counter
        - Count the frequency of all characters in the list
        - The output should contain all characters withh even frequencies + max(odd_freq)
        """
        freq = Counter(s)
        odd_count = 0
        length = len(s)

        for value in freq.values():
            odd_count += int(value % 2 != 0)
        
        if odd_count == 0:
            return length
            
        return length - odd_count + 1