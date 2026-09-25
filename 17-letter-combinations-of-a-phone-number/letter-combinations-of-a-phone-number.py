class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        num_char = {'2': 'abc',
                    '3': 'def',
                    '4': 'ghi',
                    '5': 'jkl',
                    '6': 'mno',
                    '7': 'pqrs',
                    '8': 'tuv',
                    '9': 'wxyz',
                    }
        
        result = []
        path = []

        def backtrack(index):
            if index == len(digits):
                result.append(''.join(path))
                return
            
            curr_digit = digits[index]
            letters = num_char[curr_digit]

            for char in letters:
                path.append(char)
                backtrack(index + 1)
                path.pop()
        
        backtrack(0)
        return result