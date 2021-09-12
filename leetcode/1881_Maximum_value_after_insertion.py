#https://leetcode.com/problems/maximum-value-after-insertion/
#Complexity: O(len(n))

class Solution:
    def maxValue(self, n: str, x: int) -> str:
        if n[0]=="-":
            for i in range(1,len(n)):
                if int(n[i])>x:
                    return n[:i]+str(x)+n[i:]
        else:
            for i in range(0,len(n)):
                if int(n[i])<x:
                    return n[:i]+str(x)+n[i:]
        return n[:] + str(x)
