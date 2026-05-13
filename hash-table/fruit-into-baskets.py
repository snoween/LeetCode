class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        # Define dict = element : freq
        freq = defaultdict(int)
        max_len = 0
        l = 0
        # for loop
        for i, num in enumerate(fruits):

            # Update dict
            freq[num] += 1
            # While len(dict) > 2:
            while len(freq) > 2:
                freq[fruits[l]] -= 1
                
                if freq[fruits[l]] == 0:
                    del freq[fruits[l]]

                # dict[key[left]] -= 1
                # if key has value = 0 -> del key
                l += 1

            # Update max len i-k+1
            max_len = max(max_len, i-l+1)
        
        return max_len