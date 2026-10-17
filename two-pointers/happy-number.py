class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        sum_ele = 0

        while sum_ele != 1:
            sum_ele = 0
            # Convert input to str
            digits = list(str(n))

            # Calculate sum elements in n_str
            for digit in digits:
                sum_ele += (int(digit) ** 2)
            
            # Add sum elements to seen
            if sum_ele not in seen:
                seen.add(sum_ele)
            else:
                return False
            
            n = sum_ele

        return True

          

        
        