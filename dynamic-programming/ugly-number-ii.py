class Solution:
    def nthUglyNumber(self, n: int) -> int:
        def isUglyNum(arr, num):
            if num % 2 == 0 or num % 3 == 0 or num % 5 == 0:
                print(num)
                return arr.append(num)
        
        arr = [1]
        init_num = 1
        while len(arr) < n:
            init_num += 1
            isUglyNum(arr, init_num)
            print(arr)
        
        return arr[n-1]