class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        target = Counter(nums2)
        result = []

        for num in nums1:
            if num in target and target[num] > 0:
                result.append(num)
                target[num] -= 1
        
        return result