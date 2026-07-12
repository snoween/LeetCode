class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        lo, hi = min(start, destination), max(start, destination)
        
        path = sum(distance[lo:hi])   
        total = sum(distance)         
        
        return min(path, total - path)