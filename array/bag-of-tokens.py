class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        score = 0
        tokens.sort()
        
        if power < tokens[0]:
            return score
        
        l, r = 0, len(tokens) - 1
        while l < r:
            if power >= tokens[l]:  # Face up
                print(l, power, tokens[l])
                score += 1
                power -= tokens[l]
                l += 1

            if l != r and power < tokens[r]:
                print(power, r, tokens[r])
                score -= 1
                power += tokens[r]
                r -= 1
            
            if l == r and power >= tokens[r]:
                score += 1
                  
        return score

