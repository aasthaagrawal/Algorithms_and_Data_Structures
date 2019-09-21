#https://leetcode.com/problems/reverse-integer/
#Complexity=(len(x))

class Solution:
    def reverse(self, x: int) -> int:
        result=0
        i=0
        neg=False
        if x<0:
            neg=True
            x*=(-1)
        while(x):
            result=result*10 + (x%10)
            x=int(x/10)
        if result<(-(2**31)) or result>(2**31-1):
            return 0
        return (result if neg is False else result*(-1) )
