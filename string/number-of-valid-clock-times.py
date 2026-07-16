class Solution:
    def countTime(self, time: str) -> int:
        def checkHour(index_hr1, index_hr2):
            if index_hr1 == '?' and index_hr2 == '?':
                return 24
            elif index_hr1 == '?' and int(index_hr2) >= 4:
                return 2
            elif index_hr1 == '?' and int(index_hr2) < 4:
                return 3
            elif index_hr2 == '?' and int(index_hr1) < 2:
                return 10
            elif index_hr2 == '?' and int(index_hr1) == 2:
                return 4
        
        def checkMin(index_min1, index_min2):
            print(index_min1, index_min2)
            if index_min1 == '?' and index_min2 == '?':
                return 60
            elif index_min1 == '?' and index_min2 != '?':
                return 6
            elif index_min2 == '?' and index_min1 != '?':
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
         
