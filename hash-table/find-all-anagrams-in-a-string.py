class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        lenS, lenP = len(s), len(p)
        target = Counter(p)
        curr = Counter(s[:lenP])

        result = [0] if curr == target else []

        left = 0
        for right in range(lenP, lenS):
            curr[s[right]] += 1
            curr[s[left]] -= 1

            if curr == target:
                result.append(left + 1)
            
            left += 1
        
        return result