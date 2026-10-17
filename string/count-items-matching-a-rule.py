class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        search_dict = {'type': 0,
                        'color': 1,
                        'name': 2,
                        }
        count = 0
        fea_idx = search_dict[ruleKey]

        for item in items:
            if item[fea_idx] == ruleValue:
                count += 1
        
        return count