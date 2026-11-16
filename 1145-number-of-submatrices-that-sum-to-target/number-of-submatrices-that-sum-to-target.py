class Solution:
    def numSubmatrixSumTarget(self, matrix: list[list[int]], target: int) -> int:
        """
        Solution: prefix sum on each row
        - Calculate the sum between 2 fixed columns, iterate by row
        - Check if curr_sum - target (this one is like curr_sum is sum from i -> j:
         prefix[j] - random prefix[i] = target) in hashmap or not
        - if in hashmap, means we have sum[i, j] = target -> update count += hashmap[curr_sum - target]
        - if not in hashmap -> update it with init value = 1

        Time comp: O(M * N^2)
        Space comp: O(1) for managing in-place, O(M * N) for hashmap
        """
        m, n = len(matrix), len(matrix[0])
        count = 0

        # Calculate the prefix sum of each row in the matrix
        for i in range(m):
            for j in range(1, n):
                matrix[i][j] += matrix[i][j - 1] 
        
        # Calculate the sum between 2 fixed columns
        for c1 in range(n):
            for c2 in range(c1, n):
                curr_sum = 0
                # define frequency hashmap, renew when (c1, c2) is changed
                prefix_count = {0: 1}

                # calculate the sum from c1 -> c2
                for r in range(m):
                    # update curr_sum 
                    curr_sum += matrix[r][c2] - (matrix[r][c1 - 1] if c1 > 0 else 0)
                    # calculate the starting prefix
                    prefix_start = curr_sum - target
                    if prefix_start in prefix_count:
                        count += prefix_count[prefix_start]

                    # update frequency of curr_sum to +1
                    prefix_count[curr_sum] =  prefix_count.get(curr_sum, 0) + 1
        
        return count