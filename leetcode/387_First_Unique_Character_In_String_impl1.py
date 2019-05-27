#https://leetcode.com/problems/first-unique-character-in-a-string/
#Complexity: O(n)

class Solution:
    def firstUniqChar(self, s: str) -> int:
        dict={}
        for ch in s:
            if ch in dict:
                dict[ch]+=1
            else:
                dict[ch]=1
        lenS=len(s)
        for i in range(lenS):
            if dict[s[i]]==1:
                return i
        return -1
