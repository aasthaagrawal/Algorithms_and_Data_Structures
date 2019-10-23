#https://leetcode.com/problems/coin-change/
#Complexity: O(amount*len(coins))

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp=[float('inf') for i in range(amount+1)]
        dp[0]=0
        for i in range(amount+1):
            for j in coins:
                if j<=i:
                    dp[i]=min(1+dp[i-j],dp[i])
        if dp[amount]==float('inf'):
            return -1
        return dp[amount]   
