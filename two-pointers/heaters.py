class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        best_radius, dist = 0, 0
        location = [0 * i for i in range(max(houses[-1], heaters[-1]))]

        # Get binary list of pos has heater
        for heater in heaters:
            location[heater-1] = 1
        
        first_heater = heaters[0] - 1

        if first_heater != 0:
            best_radius = first_heater

        # Calculate max distance between 2 number 1s
        for i, num in enumerate(location):
            if num == 1 and i != first_heater:
                dist = (i - first_heater-1) // 2
                first_heater = i
                best_radius = max(best_radius, dist)

        if first_heater != len(location) - 1:
            dist = len(location) - 1 - first_heater
            best_radius = max(best_radius, dist)

        return best_radius
