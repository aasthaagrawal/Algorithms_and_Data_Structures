#https://leetcode.com/problems/longest-palindromic-subsequence/
#Time Complexity: O(n^2)

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[0 for j in range(n)] for i in range(n)]

        result = 1
        for i in range(n):
            dp[i][i] = 1
            if i<n-1:
                dp[i][i+1] = 1
                if s[i] == s[i+1]:
                    result = 2
                    dp[i][i+1] = 2

        for l in range(3,n+1):
            for i in range(n-l+1):
                j = i+l-1
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] + 2
                    result = max(result, dp[i][j])
                else:
                    dp[i][j] = max(dp[i+1][j],dp[i][j-1])
        return result
