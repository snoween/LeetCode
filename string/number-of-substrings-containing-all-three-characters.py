class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        freq = defaultdict(int)
        l = 0
        count = 0
        # for loop
        for char in s:
            # Update freq 
            freq[char] += 1
            # while key a,b,c >= 1
            while freq['a'] >= 1 and freq['b'] >= 1 and freq['c'] >= 1:
                freq[s[l]] -= 1
                # update left
                l += 1
            
            # update count += l
            count += l
    
        return count