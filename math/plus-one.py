class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] != 9:
            digits[-1] += 1
            return digits
        
        else:
            num = ''.join(str(i) for i in digits)
            return [int(digit) for digit in str(int(num) + 1)]