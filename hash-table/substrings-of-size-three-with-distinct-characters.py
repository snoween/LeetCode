class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        curr_arr = Counter(s[:3])
        count = int(len(curr_arr) == 3)

        left = 0
        for right in range(3, len(s)):
            curr_arr[s[right]] += 1
            curr_arr[s[left]] -= 1

            if curr_arr[s[left]] == 0:
                del curr_arr[s[left]]
                
            left += 1
            count += int(len(curr_arr) == 3)

        return count
