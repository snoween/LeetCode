class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        freq, dist = 0, 0
        # tao 1 cai dict: "{do chenh lech chan le: idx lan dau tien}"
        diff = defaultdict(int, {0: -1})
        # for loop tinh freq chan le
        for i, num in enumerate(nums):
            if num % 2 == 0:
                freq -= 1
            else:
                freq += 1
            # khi key not in dict
            if freq not in diff:
                # cap nhat dict freq 
                diff[freq] = i
            # Else
            else:
                # cap nhat max dist = max(dist, j-i+1)
                dist = max(dist, i - diff[freq])

        return dist