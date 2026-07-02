class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        ifFirstTime = True
        stack = []
        left = 0
        right = 0

        for i, char in enumerate(word):
            if char == ch and ifFirstTime:
                stack.append(char)
                right = len(stack) - 1

                while left < right:
                    stack[left], stack[right] = stack[right], stack[left]
                    left += 1
                    right -= 1
                    
                ifFirstTime = False
            else:
                stack.append(char)
        
        return ''.join(stack)