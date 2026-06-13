class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = ['+', '-', '*', '/']

        for ele in tokens:
            if ele not in ops:
                stack.append(int(ele))
            else:
                ele1 = stack.pop()
                ele2 = stack.pop()
                if ele == '+':
                    stack.append(ele1 + ele2)
                if ele == '-':
                    stack.append(ele2 - ele1)
                if ele == '*':
                    stack.append(ele1 * ele2)
                if ele == '/':
                    stack.append(int(ele2/ele1))
        
        return stack[0]