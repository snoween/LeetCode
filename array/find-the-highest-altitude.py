class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        output = [0] + gain
        for i in range(1, len(output)):
            output[i] += output[i - 1]
        
        return max(output)