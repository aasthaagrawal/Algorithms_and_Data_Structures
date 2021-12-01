#https://leetcode.com/problems/minimum-insertion-steps-to-make-a-string-palindrome/
#Time complexity: O(n^2)
#Space complexity: O(n^2)

class Solution:

    def minInsertions(self, s: str) -> int:
        n = len(s)
        dp = [[0 for j in range(n)] for i in range(n)]
        for i in range(n-1):
            if s[i] != s[i+1]:
                dp[i][i+1] = 1
        for l in range(3,n+1):
            for i in range(n-l+1):
                j = i+l-1
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1]
                else:
                    dp[i][j] = 1 + min(dp[i+1][j], dp[i][j-1])
        return dp[0][-1]
