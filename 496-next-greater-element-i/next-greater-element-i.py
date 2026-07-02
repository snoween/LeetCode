class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n1, n2 = len(nums1), len(nums2)
        result = [-1] * n1
        
        stack = []      # store index
        nextGreater = defaultdict()

        # Find greater of each num in nums2
        for i, num in enumerate(nums2):
            while len(stack) > 0 and nums2[i] > nums2[stack[-1]]:
                popped_idx = stack.pop()
                nextGreater[nums2[popped_idx]] = nums2[i]

            stack.append(i)

        # Parse the result to match with nums1
        for i, num in enumerate(nums1):
            if num in nextGreater:
                result[i] = nextGreater[num]
            else:
                result[i] = -1
        
        return result