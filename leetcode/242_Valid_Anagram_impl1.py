#https://leetcode.com/problems/valid-anagram/
#Complexity:

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        t2=''.join(sorted(t))
        s2=''.join(sorted(s))
        if t2 == s2:
            return True
        return False
