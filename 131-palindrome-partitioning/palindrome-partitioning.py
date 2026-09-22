class Solution:
    def is_palindrome(self, sub_str):
        left, right = 0, len(sub_str) - 1

        while left <= right:
            if sub_str[left] != sub_str[right]:
                return False
            left += 1
            right -= 1

        return True

    def partition(self, s: str) -> list[list[str]]:
        result = []
        path = []

        def backtrack(start_idx):
            if start_idx >= len(s):     # Done 1 time checking all str
                result.append(path[:])

            for end in range(start_idx, len(s)):
                sub_str = s[start_idx:end+1]

                if self.is_palindrome(sub_str):
                    path.append(sub_str[:])
                    backtrack(end + 1)
                    path.pop()
        
        backtrack(0)
        return result