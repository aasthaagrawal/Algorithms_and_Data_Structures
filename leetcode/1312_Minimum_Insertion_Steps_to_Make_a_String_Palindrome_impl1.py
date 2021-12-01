#https://leetcode.com/problems/minimum-insertion-steps-to-make-a-string-palindrome/
#Time Complexity: O(n^2)
#Space Complexity: O(n^2)

class Solution:
    from functools import lru_cache

    @lru_cache(None)
    def minInsertions(self, s: str) -> int:
        if len(s) == 1 or s == "":
            return 0
        if s[0] == s[-1]:
            return 0 + self.minInsertions(s[1:-1])
        return 1 + min(self.minInsertions(s[0:-1]), self.minInsertions(s[1:]))
