#https://leetcode.com/problems/first-unique-character-in-a-string/
#Complexity: O(1)

class Solution:
    def firstUniqChar(self, s: str) -> int:
        result=len(s)
        alphabets="abcdefghijklmnopqrstuvwxyz"
        for ch in alphabets:
            firstFind=s.find(ch)
            if firstFind==-1:
                continue
            if firstFind==s.rfind(ch):
                result=min(result,firstFind)
        if result==len(s):
            return -1
        return result
