class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        odd_indices, even_indices = [], []

        for i, num in enumerate(nums):
            if i % 2 == 0:
                even_indices.append(num)
            else:
                odd_indices.append(num)
        
        odd_indices.sort(reverse=True)
        even_indices.sort()

        def merge(even, odd):
            i = j = 0
            out = []

            while i < len(even) and j < len(odd):
                out.append(even[i])
                out.append(odd[j])
                i += 1
                j += 1 

            # append leftovers
            out.extend(even[i:])
            out.extend(odd[j:])
            return out

        return merge(even_indices, odd_indices)