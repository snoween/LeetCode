class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        """
        - sort list -> [1 2 2 3 8]
        1: 0
        2[1]: 1
        2[2]: 1 
        3: 3
        8: 4
        """
        temp = nums.copy()
        temp.sort()
        smaller = defaultdict(int)

        for i in range(1, len(temp)):
            if temp[i] == temp[i - 1]:
                smaller[temp[i]] = smaller[temp[i - 1]]
            else:
                smaller[temp[i]] = i
        
        output = []
        for num in nums:
            output.append(smaller[num])
        
        return output

