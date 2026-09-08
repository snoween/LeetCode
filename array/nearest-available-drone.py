class Solution:
    def nearestDrone(self, drones: list[list[int]], target: list[int]) -> int:
        curr_min = (float(inf), float(inf))

        # loop through drone
        for i, drone in enumerate(drones):
            x, y, length = drone
            dist = abs(x - target[0]) + abs(y - target[1])
            if dist <= length:
                curr_min = min(curr_min, (dist, i))
                
        return curr_min[1] if curr_min[1] != float(inf) else -1
                