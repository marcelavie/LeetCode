class Solution(object):
    def change(self, amount, coins):
        array_coins =  [0] * (amount +1)
        array_coins[0] = 1

        for coin in coins:
            for i in range(coin, amount +1):
                array_coins[i] += array_coins[i - coin]
        return array_coins[amount]
    
# link do exercício: https://leetcode.com/problems/coin-change-ii/description/