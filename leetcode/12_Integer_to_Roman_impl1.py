#https://leetcode.com/problems/integer-to-roman/
#Complexity: O(n)

class Solution:
    def intToRoman(self, num: int) -> str:
        pos=0
        result=""
        while num:
            digit=num%10
            num=int(num/10)
            result=self.findNumeral(digit,pos)+result
            pos+=1
        return result
            
    def findNumeral(self,digit,pos):
        res=""
        if pos==0:
            if digit<4:
                for i in range(digit):
                    res=res+"I"
            elif digit==4:
                res= "IV"
            elif digit==5:
                res= "V"
            elif digit==9:
                res= "IX"
            else:
                res="V"
                for i in range(digit-5):
                    res=res+"I"
        elif pos==1:
            if digit<4:
                for i in range(digit):
                    res=res+"X"
            elif digit==4:
                res= "XL"
            elif digit==5:
                res= "L"
            elif digit==9:
                res= "XC"
            else:
                res="L"
                for i in range(digit-5):
                    res=res+"X"
        elif pos==2:
            if digit<4:
                for i in range(digit):
                    res=res+"C"
            elif digit==4:
                res= "CD"
            elif digit==5:
                res= "D"
            elif digit==9:
                res= "CM"
            else:
                res="D"
                for i in range(digit-5):
                    res=res+"C"
        elif pos==3:
            if digit<4:
                for i in range(digit):
                    res=res+"M"
        return res
