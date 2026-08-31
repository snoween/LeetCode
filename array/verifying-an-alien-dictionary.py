class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        adj = defaultdict(int)

        for i, char in enumerate(order):
            adj[char] = i
        
        for j in range(len(words) - 1):
            curr_word = words[j]
            next_word = words[j + 1]
            findDiff = False
            
            min_len = min(len(curr_word), len(next_word))
            for k in range(min_len):
                element1 = curr_word[k]
                element2 = next_word[k]

                if element1 != element2:
                    if adj[element1] > adj[element2]:
                        return False

                    findDiff = True
                    break
            
            if not findDiff and len(curr_word) > len(next_word):
                return False
            
            return True



