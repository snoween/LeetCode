class Solution:
    def maximumProduct(self, nums: list[int]) -> int:
        """
        Method: max1 * max2 * max3 and max1 * min1 * min2
        Eg: 
        Case 1: array only contains positive numbers
        -> maximum product = max1 * max2 * max3
        Case 2: array has both neg + pos nums
        -> Only has 2 types of results
        [-1 -2 3 4]
        -> min1 = -1, min2 = -2, max1 = 4, max2 = 3, max3 = -2
        -> result 1 = min1 x min2 x max1 = 8
        -> result 2 = max1 x max2 x max 3 = -24
        -> output = 8

        set up max1,2,3 = -inf; min1,2 = inf
        update 5 variables when see new num
        if num < min -> update min nums
        if num > max -> update max nums
        i = 0 -> num = -1 < min1 = inf, num > max1 -> min1 = -1, max1 = -1
        i = 1 -> num = -2 < min1 = -1 -> min2 = -2
        i = 2 -> num = 3 > max1 -> max1 = 3
        i = 3 

        - Loop through nums to find 5 values max1-3 and min1-2

        Time comp: O(N)
        Sapce comp: O(1)
        """

        max1 = max2 = max3 = float(-inf)
        min1 = min2 = float(inf)

        for num in nums:
            if num > max1:
                max3 = max2
                max2 = max1
                max1 = num
            elif num > max2:
                max3 = max2
                max2 = num
            elif num > max3:
                max3 = num
            
            if num < min1:
                min2 = min1
                min1 = num
            elif num < min2:
                min2 = num
        
        return max(max1 * max2 * max3, min1 * min2 * max1)