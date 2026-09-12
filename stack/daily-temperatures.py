class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        days = [0] * n

        stack = []
        for i in range(n):
            # pop when find next greater
            while stack and temperatures[stack[-1]] < temperatures[i]:
                idx = stack.pop()
                days[idx] = i - idx

            stack.append(i)

        return days             