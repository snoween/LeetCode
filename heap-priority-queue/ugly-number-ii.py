class Solution:
    def nthUglyNumber(self, n: int) -> int:
        def isUglyNum(heap, num):
            if num % 5 == 0:
                heapq.heappush(arr, num * 5)
                return arr
            elif num % 3 == 0:
                heapq.heappush(arr, num * 3)
                heapq.heappush(arr, num * 5)
                return arr
            elif num % 2 == 0 or num == 1:
                heapq.heappush(arr, num * 2)
                heapq.heappush(arr, num * 3)
                heapq.heappush(arr, num * 5)
                return arr
        
        arr = [1]
        heapq.heapify(arr)

        count = 1
        while count < n:
            num = heapq.heappop(arr)
            isUglyNum(arr, num)
            count += 1
        
        return heapq.heappop(arr)