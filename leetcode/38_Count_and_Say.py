#https://leetcode.com/problems/count-and-say/
#Complexity: 

class Solution:
    def countAndSay(self, n: int) -> str:
        string="1"
        newStr=""
        i=1
        count=0
        while i<n:
            strLen=len(string)
            j=0
            while j<strLen:
                if j==0:
                    count=1
                elif string[j]==string[j-1]:
                    count+=1
                else:
                    newStr+=str(count)+str(string[j-1])
                    count=1
                j+=1
            newStr+=str(count)+str(string[j-1])
            string=newStr
            newStr=""
            i+=1
        return string
