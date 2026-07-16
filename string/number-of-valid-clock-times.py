class Solution:
    def countTime(self, time: str) -> int:
        def checkHour(h1, h2):
            if h1 == '?' and h2 == '?':
                return 24
            elif h1 == '?' and int(h2) >= 4:
                return 2
            elif h1 == '?' and int(h2) < 4:
                return 3
            elif h2 == '?' and int(h1) < 2:
                return 10
            elif h2 == '?' and int(h1) == 2:
                return 4
        
        def checkMin(m1, m2):
            if m1 == '?' and m2 == '?':
                return 60
            elif m1 == '?' and m2 != '?':
                return 6
            elif m2 == '?' and m1 != '?':
                return 10
        
        time_list = list(time)
        count_hr = checkHour(time_list[0], time_list[1])
        count_min = checkMin(time_list[3], time_list[4])

        if not count_hr and not count_min:
            return 1
        elif count_hr and count_min:
            return count_hr * count_min
        elif not count_hr:
            return count_min
        elif not count_min:
            return count_hr    