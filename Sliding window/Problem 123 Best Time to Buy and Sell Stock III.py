"""Problem 123. Best Time to Buy and Sell Stock III (Difficulty: Hard).
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/

You are given an array prices where prices[i] is the price of a given stock on the ith day.
Find the maximum profit you can achieve. You may complete at most two transactions.
Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

Example 1:
Input: prices = [3,3,5,0,0,3,1,4]
Output: 6
Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.

Example 2:
Input: prices = [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are engaging multiple transactions
at the same time. You must sell before buying again.

Example 3:
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.

Constraints:
    1 <= prices.length <= 105
    0 <= prices[i] <= 105"""


class Solution123:
    def max_profit(self, prices: list[int], counter=2) -> int:
        if counter == 0:
            return 0
        buy = 0
        sell = 1
        profit_1 = 0
        profit_2 = 0
        max_profit = profit_1
        while buy < len(prices) and sell < len(prices):
            if prices[sell] >= prices[buy]:
                difference = prices[sell] - prices[buy]
                current_profit = 0
                current_profit = max(current_profit, difference)
                profit_index = sell
                profit_1 = current_profit
                if max_profit < current_profit:
                    max_profit = current_profit
                sell += 1
                new_prices = prices[profit_index + 1:]
                profit_2 = self.max_profit(new_prices, counter-1)
            else:
                sell += 1
            if sell == len(prices):
                buy += 1
                sell = buy + 1
            max_profit = max(max_profit, profit_1 + profit_2)
        return max_profit


solution = Solution123()
print(solution.max_profit([3, 3, 5, 0, 0, 3, 1, 4]))
print(solution.max_profit([1, 2, 3, 4, 5]))
print(solution.max_profit([7, 6, 4, 3, 1]))