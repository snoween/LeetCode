class Solution:
    def maximizeSum(self, nums: list[int], k: int) -> int:
        def get_max_num(num: int):
            if num == 0:
                return 0

            count = [0] * 10
            temp = num

            while temp > 0:
                digit = temp % 10
                count[digit] += 1
                temp //= 10

            ans = 0
            for d in range(9, -1, -1):
                while count[d] > 0:
                    ans = ans * 10 + d
                    count[d] -= 1

            return ans

        total = sum(nums)

        gains = []
        for num in nums:
            max_num = get_max_num(num)
            gain = max_num - num
            if gain > 0:
                gains.append(gain)

        gains.sort(reverse=True)
        total += sum(gains[:k])

        return total