class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        # set up stack
        stack = []
        # set up count = k
        count = k
        # loop through str from tail to head
        for i in range(len(s) - 1, -1, -1):
            # if ele is char
            if s[i].isalpha():
                # stack append upper char
                stack.append(s[i].upper())
                # count - 1
                count -= 1
            
            # if ele is digit
            elif s[i].isdigit():
                # stack append string of digit
                stack.append(str(s[i]))
                # count -1
                count -= 1

            # if count = 0
            if count == 0:
                # stack append dash
                stack.append('-')
                # count = k
                count = k
        
        # check if not stack
        if not stack:
            # return ''
            return ''

        # check if the last component is dash 
        while stack and stack[-1] == '-':
            # pop dash
            stack.pop()

        # return reversed stack and join it
        return ''.join(reversed(stack))