class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        count = numBottles

        while numBottles >= numExchange:
            drink = int(numBottles / numExchange)
            remaining = int(numBottles % numExchange)
            
            count += drink
            numBottles = drink +  remaining
        
        return count