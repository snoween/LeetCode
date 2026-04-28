class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pref = [1] * n
        suf = [1] * n
        output = [1] * n

        # Get prefix of each nums[i]
        for i in range(n):
            if i > 0:
                pref[i] = pref[i-1] * nums[i-1]
        
        # Get suffix of each nums[j]
        for j in range(n-1, -1, -1):
            if j < n-1:
                suf[j] = suf[j+1] * nums[j+1]

        print(pref, suf)
        # Get the output[i] = suf[i] * pre[j]
        for i in range(n):
            output[i] = pref[i] * suf[i]
        
        return output