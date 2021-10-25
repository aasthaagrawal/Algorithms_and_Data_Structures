#https://leetcode.com/problems/split-a-string-into-the-max-number-of-unique-substrings/
#Time complexity: O(n!)

class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        return self.util(s,set())
    
    def util(self, s, seen_set):
        if not s:
            return 0
        res = 0
        len_s = len(s)
        for i in range(len(s)):
            substr = s[:i+1]
            if substr not in seen_set and len_s-i>res:
                seen_set.add(substr)
                res = max(res,1+self.util(s[i+1:], seen_set))
                seen_set.remove(substr)
        return res
