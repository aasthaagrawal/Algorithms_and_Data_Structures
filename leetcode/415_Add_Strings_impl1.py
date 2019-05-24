#https://leetcode.com/problems/add-strings/
#Complexity: O(n)

class Solution:
    def addThree(self, num1: str, num2: str, lenNum1: int, lenNum2: int):
        carry=0
        sumString=""
        while(lenNum1>=0):
            loopSum=int(num1[lenNum1],10)+int(num2[lenNum2],10)+carry
            carry=loopSum//10
            sumAtIndex=loopSum%10
            sumString="%d%s" % (sumAtIndex,sumString)
            lenNum1-=1
            lenNum2-=1
        return sumString,carry,lenNum2
    
    def addTwo(self,num: str, sumString: str, carry: int, length:int):
        while(length>=0):
            loopSum=int(num[length],10)+carry
            carry=loopSum//10
            sumAtIndex=loopSum%10
            sumString="%d%s" % (sumAtIndex,sumString)
            length-=1
        return sumString,carry
    
    def addStrings(self, num1: str, num2: str) -> str:
        lenNum1=len(num1)
        lenNum2=len(num2)
        sumString=""
        carry=0
        if lenNum1<lenNum2:
            sumString, carry,length = self.addThree(num1,num2,lenNum1-1,lenNum2-1)
            sumString, carry = self.addTwo(num2,sumString,carry,length)
        elif lenNum1==lenNum2:
            sumString, carry, length = self.addThree(num1,num2,lenNum1-1,lenNum2-1)
        else:
            sumString, carry, length = self.addThree(num2,num1,lenNum2-1,lenNum1-1)
            sumString, carry = self.addTwo(num1,sumString,carry,length)
            
        if carry>0:
            sumString="%d%s" % (carry,sumString)
        return sumString
