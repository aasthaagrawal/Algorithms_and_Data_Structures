#https://leetcode.com/problems/zigzag-conversion/
#Complexity:

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1 or numRows>=len(s):
            return s
        result=[""]*numRows
        j=0
        movement=1
        for i in s:
            result[j]+=i
            if j==numRows-1:
                movement=-1
            elif j==0:
                movement=1
            j+=movement
        return ''.join(result)
