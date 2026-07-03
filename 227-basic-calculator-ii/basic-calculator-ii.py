class Solution:
    def calculate(self, s: str) -> int:
        operation = {'+': lambda a, b: a + b, 
                '-': lambda a, b: a - b,
                '*': lambda a, b: a * b,
                '/': lambda a, b: int(a / b)}

        stack = []
        currentNumber = 0
        result = 0
        sign = '+'

        for i, char in enumerate(s):
            if char.isdigit():
                currentNumber = currentNumber * 10 + int(char)
            
            if char in operation or i == len(s) - 1:
                if sign == '+':
                    stack.append(currentNumber)
                elif sign == '-':
                    stack.append(-currentNumber)
                elif sign == '*' or sign == '/':
                    previousNumber = stack.pop()
                    stack.append(operation[sign](previousNumber, currentNumber))
                
                sign = char
                currentNumber = 0
        
        for num in stack:
            result += num
        
        return result
