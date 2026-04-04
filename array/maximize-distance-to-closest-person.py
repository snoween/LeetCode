class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        k = 0
        dist = 0
        best_dist = 0 
        
        for i in range(len(seats)):
            if seats[i] == 1 and seats[k] == 1:
                dist = i - ((i + k) // 2)
                k = i
            
            elif seats[i] == 1 and seats[k] == 0:
                dist = i - k
                k = i
            
            elif i == len(seats) - 1 and seats[i] == 0:
                dist = i - k

            best_dist = max(best_dist, dist)
        
        return best_dist           