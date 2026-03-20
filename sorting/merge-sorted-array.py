class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i, j = len(nums1) - 1, n - 1

        while i >= 0:
            print(i, j)
            if nums1[i] < nums2[j] and j >= 0:
                nums1[i] = nums2[j]
                j -= 1
                i -= 1
            
            elif j != 0:
                if nums1[i] > nums1[i + 1]:
                    nums1[i], nums1[i + 1] = nums1[i + 1], nums1[i]
                i -= 1
        
        
        