class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        adj = defaultdict()

        for i in range(len(order) - 1):
            adj[order[i]] = set(order[i + 1::])
        
        for j in range(len(words) - 1):
            curr_word = words[j]
            next_word = words[j + 1]
            min_len = min(len(curr_word), len(next_word))

            for k in range(min_len):
                if curr_word[k] != next_word[k]:
                    if next_word[k] not in adj[curr_word[k]]:
                        return False
                    break
            else:
                if len(curr_word) > len(next_word):
                    return False
               
        return True