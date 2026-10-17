class Solution:
    def lemonadeChange(self, bills: list[int]) -> bool:
        listOfBills = [10, 5]
        count = defaultdict(int)

        for num in bills:
            count[num] += 1
            change = num - 5

            for bill in listOfBills:
                numOfBills = min(count[bill], change // bill)
                count[bill] -= numOfBills
                change -= bill * numOfBills
                if change == 0:
                    break
            
            if change != 0: 
                return False

        return True