#https://leetcode.com/problems/length-of-last-word/
#Complexity: O(n)
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s=s.rstrip()
        sn=s.split(' ')
        print(sn)
        lw=sn[len(sn)-1]
        if(lw!=""):
            return len(lw)
        else:
            return 0
