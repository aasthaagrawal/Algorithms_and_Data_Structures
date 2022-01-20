#https://leetcode.com/problems/regular-expression-matching/
#Time complexity: O(MN) where M is the length of s and N is the length of p
#Space complexity: O(MN) where M is the length of s and N is the length of p

class Solution:
    from functools import lru_cache

    @lru_cache(None)
    def isMatch(self, s: str, p: str) -> bool:
        if not p:
            return not s

        first_match = bool(s) and p[0] in {s[0], '.'}

        if len(p) >= 2 and p[1] == '*':
            return self.isMatch(s, p[2:]) or (first_match and self.isMatch(s[1:], p))
        else:
            return first_match and self.isMatch(s[1:], p[1:])
