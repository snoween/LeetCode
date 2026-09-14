class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        Solution: Find the starting number 
        - Starting number = Current number - 1
        - Update the length while curr_num + 1 in nums
        """
        if not nums:
            return 0

        parent = {num: num for num in nums}
        size = {num: 1 for num in nums}

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            parentX, parentY = find(x), find(y)

            if parentX == parentY:
                return

            if size[parentX] < size[parentY]:
                parent[parentX] = parentY
                size[parentY] += size[parentX]
            else:
                parent[parentY] = parentX
                size[parentX] += size[parentY]
        
        # loop through parent
        for num in parent:
            if num - 1 in parent:
                union(num, num - 1)

        return max(size.values())