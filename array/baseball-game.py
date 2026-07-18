class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
   
        for ele in operations:
            if ele == 'C':
                stack.pop()
            elif ele == 'D':
                stack.append(stack[-1] * 2)
            elif ele == '+':
                num1 = stack[-1]
                num2 = stack[-2]
                stack.append(num1 + num2)
            else:
                stack.append(int(ele))

        output = 0
        for num in stack:
            output += num
        
        return output