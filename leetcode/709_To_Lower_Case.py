#https://leetcode.com/problems/to-lower-case/
#Complexity: O(n)

class Solution:
    def toLowerCase(self, str: str) -> str:
        lenString=len(str)
        i=0
        for i in range(lenString):
            ordI=ord(str[i])
            if ordI>=65 and ordI<=90:
                str=str[:i]+chr(32+ordI)+str[i+1:]
            i+=1
        return str
