class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        even = [num for num in nums if num %2 == 0]
        odd = [num for num in nums if num %2 != 0]

        output = [0 for _ in range(len(nums))]
        k, v = 0, 0

        for i in range(len(output)):
            if i % 2 == 0:
                output[i] = even[k]
                k += 1
            else:
                output[i] = odd[v]
                v += 1
        
        return output