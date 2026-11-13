class NumArray:

    def __init__(self, nums: list[int]):
        n = len(nums)
        self.prefix = [0] * n
        for i in range(n):
            if i > 0:
                self.prefix[i] = self.prefix[i - 1] + nums[i]
            else:
                self.prefix[i] = nums[i]

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.prefix[right]
        return self.prefix[right] - self.prefix[left - 1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)