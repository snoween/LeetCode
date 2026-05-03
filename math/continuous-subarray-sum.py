class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        prefix = [0] * n
        # tao 1 dict co nghia la "remainder: idx dau tien ma co remainder nay"
        remain_dict = defaultdict(int)
        # dung for loop de tinh  prefix
        for i in range(n):
            # tinh mod cua prefix
            prefix[i] = (prefix[i-1] if i > 0 else 0) + nums[i]
            rem = prefix[i] % k
            # check xem la cai mod co nam trong dict chua
            if rem in remain_dict:
            # neu co:
                #check khoang cah:
                if i - remain_dict[rem] > 1:
                    # return true neu dung
                    return True
            # neu khong:
            else:
                # update mod res + ind vo dict {i: res}
                remain_dict[rem] = i
        # return False
        return False
        