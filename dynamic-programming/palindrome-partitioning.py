class Solution:
    def partition(self, s: str) -> list[list[str]]:
        result = []
        path = []

        def is_palindrome(sub_str):
            left, right = 0, len(sub_str) - 1
            while left <= right:
                if sub_str[left] == sub_str[right]:
                    left += 1
                    right -= 1
                else:
                    return False
            return True

        def backtrack(start):
            if start >= len(s):
                result.append(path[:])
                return
            
            for end in range(start, len(s)):
                sub_str = s[start:end + 1]

                if is_palindrome(sub_str):    # Check if palindrome, can compare sub_str == sub_str[::-1], no need 2 pointers if lazy
                    path.append(sub_str)
                    backtrack(end + 1)
                    path.pop()
        
        backtrack(0)
        return result
