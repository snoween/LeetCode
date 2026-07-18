class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for ele in operations:
            print(stack)
            if ele[0] == '-' or ele.isdigit():
                stack.append(int(ele))
            elif ele == 'C':
                stack.pop()
            elif ele == 'D':
                stack.append(stack[-1] * 2)
            elif ele == '+':
                num1 = stack[-1]
                num2 = stack[-2]
                stack.append(num1 + num2)
        
        output = 0
        for num in stack:
            output += num
        
        return output