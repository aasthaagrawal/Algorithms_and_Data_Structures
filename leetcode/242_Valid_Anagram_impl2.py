#https://leetcode.com/problems/valid-anagram/
#Complexity:

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_t={x: t.count(x) for x in set(t)}
        dict_s={x: s.count(x) for x in set(s)}
        if dict_s==dict_t:
            return True
        return False
