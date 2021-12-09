#https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/
#Time complexity: O(n)
#Space complexity: O(n)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n <= 1:
            return 0
        dp = [0]*n
        lowest_price = prices[0]
        for i in range(1,n):
            if prices[i]<lowest_price:
                lowest_price = prices[i]
            dp[i] = max(dp[i-1], prices[i]-lowest_price)

        max_profit = 0
        highest_price = prices[n-1]
        right_max_profit = 0
        for i in range(n-2,-1,-1):
            if prices[i] > highest_price:
                highest_price = prices[i]
            right_max_profit = max(right_max_profit, highest_price - prices[i])
            dp[i] += right_max_profit
            max_profit = max(max_profit, dp[i])
        return max_profit
