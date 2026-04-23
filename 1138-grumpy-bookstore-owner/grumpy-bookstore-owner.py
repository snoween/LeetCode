class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        n = len(customers)
        # Find the time that can convert the most satisfied customers
        curr_mood = sum(grumpy[:minutes])
        curr_pp = sum(customers[i] for i, num in enumerate(grumpy[:minutes]) if num == 1)
        most_pp = curr_pp
        worst_mood = curr_mood
        best_idx = 0
        output = 0

        for r in range(minutes, n):
            print(curr_mood)
            curr_mood = curr_mood + grumpy[r] - grumpy[r-minutes]
            if grumpy[r] == 1:
                curr_pp = curr_pp + customers[r]
            if grumpy[r-minutes] == 1:
                curr_pp -= customers[r-minutes]

            most_pp = max(most_pp, curr_pp)
            worst_mood = max(worst_mood, curr_mood)
        
        print(most_pp, best_idx)
        for i in range(n):
            if grumpy[i] == 0:
                output += customers[i]
        
        return output + most_pp
        