class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        seen = set()
        ans = 0

        # tăng right từ 0 -> cuối (trỏ vào char nằm cuối cùng trong window):
        for r, char in enumerate(s):

            #remove thanwfg char ra khoir seen trc
            while char in seen:
                seen.remove(s[l])
                l += 1

            # giaxn window theem r nayf
            seen.add(char)
            #cập nhật đồ dài lớn nhất có thể
            ans = max(ans, r - l + 1)

        return ans