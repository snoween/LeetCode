class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        even = [num for num in nums if num %2 == 0]
        odd = [num for num in nums if num %2 != 0]

        output = [0 for _ in range(len(nums))]
        i, k, v = 0, 0, 0

        while i < len(output):
            output[i] = even[k]
            k += 1
            i += 1

            output[i] = odd[v]
            v += 1
            i += 1
        
        return output