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

        # calculate the prefix sum for each row
        for i in range(m):
            for j in range(1, n):
                matrix[i][j] += matrix[i][j - 1]
        
        # Calculate the sum of the matrix between 2 columns
        for c1 in range(n):
            for c2 in range(c1, n):
                curr_sum = 0
                prefix_count = {0: 1}

                for r in range(m):
                    # curr_sum = prefix[right] - prefix[left - 1]
                    curr_sum += matrix[r][c2] - (matrix[r][c1 - 1] if c1 > 0 else 0)
                    prefix_left = curr_sum - target

                    # update count if valid sum of prefix[right], prefix[left]
                    if prefix_left in prefix_count:
                        count += prefix_count[prefix_left]
                    
                    # add curr_sum to prefix_count
                    prefix_count[curr_sum] = prefix_count.get(curr_sum, 0) + 1

        return count