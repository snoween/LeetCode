class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums_circular = nums + nums
        next_larger = [-1] * n * 2

        stack = []
        for i in range(n * 2):
            while stack and nums_circular[stack[-1]] < nums_circular[i]:
                idx = stack.pop()
                next_larger[idx] = nums_circular[i]
            stack.append(i)
        
        return next_larger[:n]