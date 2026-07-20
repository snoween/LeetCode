class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
   
        for ele in operations:
            if ele == 'C':
                stack.pop()
            elif ele == 'D':
                stack.append(stack[-1] * 2)
            elif ele == '+':
                stack.append(stack[-1] + stack[-2])
            else:
                stack.append(int(ele))

        output = 0
        for num in stack:
            output += num
        
        return output