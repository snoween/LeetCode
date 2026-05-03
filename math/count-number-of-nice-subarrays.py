class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        curr = 0
        count = 0
        # update dict{number of odd: idx first meet}
        odd_idx = defaultdict(lambda: -1)

        # For loop to iterate getting curr_odd at i
        for i, num in enumerate(nums):
            if num % 2 == 1:
                # update curr (number of odd)
                curr += (num % 2)
                # chi update dict neu so hien tai tai i la le
                odd_idx[curr] = i
            # count += dict[curr - k + 1] - dict[curr - k] + 1
            count += odd_idx[curr - k + 1] - odd_idx[curr - k] 
            print(curr, count)

        print(odd_idx)
        return count