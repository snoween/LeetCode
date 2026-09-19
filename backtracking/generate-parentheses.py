class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        freq = {'(': n,
                ')': n}
        
        result = []
        path = []

        def backtrack():
            if freq['('] == 0 and  freq[')'] == 0:
                result.append(''.join(path))
                return
            
            if freq['('] > 0:
                path.append('(')
                freq['('] -= 1
                backtrack()
                freq['('] += 1
                path.pop()
            
            if freq[')'] > freq['(']:
                path.append(')')
                freq[')'] -= 1
                backtrack()
                freq[')'] += 1
                path.pop()
        
        backtrack()
        return result