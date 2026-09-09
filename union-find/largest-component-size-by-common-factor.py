class Solution:
    def largestComponentSize(self, nums: List[int]) -> int:
        # get the min common factor ò each number from 0 - max num
        max_num = max(nums)
        common_factor = list(range(max_num + 1))

        # loop until rms(n)
        p = 2
        while (p * p) <= max_num:
            for i in range(p * p, max_num + 1, p):    # common multiple is not prime num
                if common_factor[i] == i:
                    common_factor[i] = p
            p += 1
        
        print(common_factor)
        # build parent, size
        parent = {}
        size = {}

        def find(x):
            # check if x in parent or not
            if x not in parent:
                parent[x] = x
                size[x] = 1

            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            parentX, parentY = find(x), find(y)

            if parentX == parentY:
                return False
            
            if size[parentX] < size[parentY]:
                parent[parentX] = parentY
                size[parentY] += size[parentX]
            else:
                parent[parentY] = parentX
                size[parentX] += size[parentY]
            
            return True

        for num in nums:
            temp = num
            while temp > 1:
                prime = common_factor[temp]
                union(num, prime)
                while temp % prime == 0:
                    temp //= prime

        root_count = Counter()
        for num in nums:
            root_count[find(num)] += 1
        
        return max(root_count.values())