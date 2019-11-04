#https://leetcode.com/problems/longest-palindromic-substring/

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        n=len(s)
        dp=[[False for j in range(n)] for i in range(n)]
        start=0
        maxLen=1
        for i in range(n):
            dp[i][i]=True
        for i in range(n-1):
            if s[i]==s[i+1]:
                dp[i][i+1]=True
                maxLen=2
                start=i
            else:
                dp[i][i+1]=False
        for k in range(3,n+1):
            for i in range(n-k+1):
                j=i+k-1
                if s[i]==s[j] and dp[i+1][j-1]:
                    dp[i][j]=True
                    maxLen=k
                    start=i
                else:
                    dp[i][j]=False
        return s[start:maxLen+start]
