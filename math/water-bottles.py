class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        count = numBottles
        while numBottles >= numExchange:
            print(numBottles)
            count += int(numBottles / numExchange)
            numBottles = int(numBottles / numExchange) +  int(numBottles % numExchange)
        
        return count