class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        score, max_score = 0, 0
        tokens.sort()
        
        l, r = 0, len(tokens) - 1

        while l <= r:
            if power >= tokens[l]:  # Face down
                score += 1
                power -= tokens[l]
                l += 1

                max_score = max(max_score, score)

            elif score > 0:
                score -= 1
                power += tokens[r]
                r -= 1

            else:
                break

        return max_score