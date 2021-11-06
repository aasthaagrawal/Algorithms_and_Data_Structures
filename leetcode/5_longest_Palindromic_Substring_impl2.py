#https://leetcode.com/problems/longest-palindromic-substring/
#Time limit exceeds

class Solution:
    from functools import lru_cache
    def longestPalindrome(self, s: str) -> str:
        self.maxLen = 1
        self.start = 0
        n = len(s)

        @lru_cache(None)
        def dp(i,j):
            if i==j:
                return True
            if i+1 == j:
                if s[i] == s[j]:
                    if self.maxLen < j-i+1:
                        self.maxLen = 2
                        self.start = i
                    return True
                return False
            if s[i] == s[j] and dp(i+1,j-1):
                if self.maxLen < j-i+1:
                    self.maxLen = j-i+1
                    self.start = i
                return True
            return False

        for i in range(n):
            for j in range(i,n):
                dp(i,j)
        return s[self.start:self.start + self.maxLen]
