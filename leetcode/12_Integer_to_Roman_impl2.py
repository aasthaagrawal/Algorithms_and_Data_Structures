#https://leetcode.com/problems/integer-to-roman/
#Complexity: O(n)

class Solution:
    def intToRoman(self, num: int) -> str:
        pos=0
        result=""
        numerals=[['I','V'],['X','L'],['C','D'],['M']]
        while num:
            digit=num%10
            num=int(num/10)
            res=""
            if digit<4:
                res=numerals[pos][0]*digit
            elif digit==4:
                res=numerals[pos][0]+numerals[pos][1]
            elif digit==5:
                res=numerals[pos][1]
            elif digit==9:
                res=numerals[pos][0]+numerals[pos+1][0]
            else:
                n=digit-5
                res=numerals[pos][1]+numerals[pos][0]*n
            result=res+result
            pos+=1
        return result
