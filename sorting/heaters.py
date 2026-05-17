class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        dist = 0
        best_radius = 0
        k = 0

        for house in houses:
            while k < len(heaters) - 1 and abs(house - heaters[k]) >= abs(house - heaters[k+1]):
                k += 1
                
            dist = abs(house - heaters[k])
            best_radius = max(best_radius, dist)
        
        return best_radius