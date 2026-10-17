class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pascal = []

        for i in range(numRows):
            if i == 0:
                pascal.append([1])
            else:
                # Get (i - 1)th row in matrix -> pascal[-1]
                prev_row = pascal[-1]

                new_row = []
                # Compute the next row using last row -> [1] + for loop qua i-1 rowth to compute + [1]
                for j in range(len(prev_row)-1):
                    num_to_add = prev_row[j] + prev_row[j + 1]
                    new_row.append(num_to_add)

                new_row = [1] + new_row + [1]

                # Append to the new row to pascal
                pascal.append(new_row)
            

        return pascal