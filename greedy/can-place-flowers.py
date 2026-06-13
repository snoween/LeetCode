class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        for i, num in enumerate(flowerbed):
            isLeftEmpty = i == 0 or flowerbed[i-1] == 0
            ifRightEmpty = i == len(flowerbed)-1 or flowerbed[i+1] == 0

            if isLeftEmpty and ifRightEmpty and num == 0:
                n -= 1

        return n <= 0    