class Solution:
    def change(self, amount: int, coins: list[int]) -> int:
        arr = [0] * (amount + 1)
        # with amount = 0 -> use 0 coins -> 1 way
        arr[0] = 1

        for coin in coins:
            for i in range(coin, amount + 1):
                arr[i] = arr[i] + arr[i - coin]
        
        return arr[-1]