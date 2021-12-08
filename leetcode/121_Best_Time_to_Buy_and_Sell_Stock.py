#https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
#Time complexity: O(n)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        n = len(prices) - 1
        largest_from_end = prices[n]
        n -= 1
        while n >= 0:
            if largest_from_end < prices[n]:
                largest_from_end = prices[n]
            else:
                max_profit = max(max_profit, largest_from_end-prices[n])
            n -= 1
        return max_profit
