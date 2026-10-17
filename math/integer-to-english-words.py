class Solution:
    def numberToWords(self, num: int) -> str:
        units = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        
        def SplitNum(num):
            if num == 0:
                return ""
            elif num < 20:
                return units[num]
            elif num < 100:
                if num % 10 == 0:
                    return tens[num // 10]
                else:
                    return tens[num // 10] + " " + units[num % 10]
            elif num < 1000:
                if num % 100 == 0:
                    return units[num // 100] + " Hundred"
                else:
                    return units[num // 100] + " Hundred " + SplitNum(num % 100)
            elif num < 1000000:
                if num % 1000 == 0:
                    return SplitNum(num // 1000) + " Thousand"
                else:
                    return SplitNum(num // 1000) + " Thousand " + SplitNum(num % 1000)
            elif num < 1000000000:
                if num % 1000000 == 0:
                    return SplitNum(num // 1000000) + " Million"
                else:
                    return SplitNum(num // 1000000) + " Million " + SplitNum(num % 1000000)
            else:
                if num % 1000000000 == 0:
                    return SplitNum(num // 1000000000) + " Billion"
                else:
                    return SplitNum(num // 1000000000) + " Billion " + SplitNum(num % 1000000000)

        if num == 0:
            return "Zero"
        return SplitNum(num)