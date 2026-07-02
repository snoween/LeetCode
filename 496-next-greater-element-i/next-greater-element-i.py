class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n = len(nums2)
        result = [-1] * n
        
        stack = []      # store index

        nextGreater = defaultdict()

        for i, num in enumerate(nums2):
            while len(stack) > 0 and nums2[i] > nums2[stack[-1]]:
                popped_idx = stack.pop()
                result[popped_idx] = nums2[i]
                nextGreater[nums2[popped_idx]] = result[popped_idx]
            stack.append(i)
        
        res = [-1] * len(nums1)

        for i, num in enumerate(nums1):
            if num in nextGreater:
                res[i] = nextGreater[num]
            else:
                res[i] = -1
        
        return res