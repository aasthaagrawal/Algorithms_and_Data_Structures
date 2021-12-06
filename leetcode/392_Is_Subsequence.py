#https://leetcode.com/problems/is-subsequence/
#Time complexity: O(len(t))

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        sn, tn = len(s), len(t)
        if sn == 0:
            return True
        if tn == 0:
            return False
        i, j = 0, 0
        while i < sn and j < tn:
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == sn
