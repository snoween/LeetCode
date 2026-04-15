class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        curr_dict = Counter(blocks[:k])
        best_num = curr_dict['W']
        
        for r in range(k, len(blocks)):
            curr_dict[blocks[r]] += 1
            curr_dict[blocks[r-k]] -= 1

            if curr_dict['B'] == k:
                return 0

            best_num = min(best_num, curr_dict['W'])
        
        return best_num