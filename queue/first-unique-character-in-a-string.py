class Solution:
    def firstUniqChar(self, s: str) -> int:
        # Create a dictionary to store frequencies of all characters in 's'
        freq_s = Counter(s)

        # Return index of the first character has frequency = 1
        for i, char in enumerate(s):
            if freq_s[char] == 1:
                return i

        # if no valid character has frequency = 1 --> return -1
        return -1