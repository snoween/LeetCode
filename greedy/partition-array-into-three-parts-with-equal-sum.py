class Solution:
    def canThreePartsEqualSum(self, arr: list[int]) -> bool:
        total = sum(arr)

        # check if can divide 3 parts
        if total % 3 != 0:
            return False

        target = total // 3
        foundParts = 0
        partSum = 0

        for num in arr:
            partSum += num
            if partSum == target:
                foundParts += 1
                partSum = 0

        return foundParts >= 3