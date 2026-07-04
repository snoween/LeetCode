class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        result = []

        for char in s:
            if stack and char == stack[-1][0]:
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    stack.pop()
            else:
                stack.append([char, 1])
        
        for sublist in stack:
            result.append(sublist[0]*sublist[1])
        
        return ''.join(result)