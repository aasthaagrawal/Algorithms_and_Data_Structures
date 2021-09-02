#https://leetcode.com/problems/distinct-subsequences/
#Complexity = O(slen*tlen)

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        slen = len(s)+1
        tlen = len(t)+1
        if tlen>slen:
            return 0
        
        dp = [[0 for j in range(tlen)] for i in range(slen)]
        for i in range(slen):
            dp[i][0] = 1
        
        for i in range(1,slen):
            for j in range(1,tlen):
                if s[i-1] == t[j-1]:
                    dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]
        
        return dp[-1][-1]
