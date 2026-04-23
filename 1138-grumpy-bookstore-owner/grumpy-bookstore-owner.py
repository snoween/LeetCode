class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        n = len(customers)
        # Find the time that can convert the most satisfied customers
        curr_mood = sum(grumpy[:minutes])
        curr_pp = sum(customers[i] for i, num in enumerate(grumpy[:minutes]) if num == 1)
        most_pp = curr_pp

        output = sum(customers[i] for i, num in enumerate(grumpy[:minutes]) if num == 0)
 
        for r in range(minutes, n):
            if grumpy[r] == 1:
                curr_pp = curr_pp + customers[r]
            else:
                output += customers[r]

            if grumpy[r-minutes] == 1:
                curr_pp -= customers[r-minutes]


            most_pp = max(most_pp, curr_pp)
        
        print(most_pp, output)
        return output + most_pp