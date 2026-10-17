class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        n = len(customers)
        curr_pp, output = 0, 0

        # Calculate init params in minutes val
        for i, num in enumerate(grumpy[:minutes]):
            if num == 1:
                curr_pp += customers[i]
            else:
                output += customers[i]
        
        most_pp = curr_pp

        # Find the time that can convert the most satisfied customers
        for r in range(minutes, n):
            if grumpy[r] == 1:
                curr_pp += customers[r]
            else:
                output += customers[r]

            if grumpy[r-minutes] == 1:
                curr_pp -= customers[r-minutes]

            most_pp = max(most_pp, curr_pp)

        return output + most_pp