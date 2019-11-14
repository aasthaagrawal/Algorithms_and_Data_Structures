#https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        if not s:
            return ""
        numOpen=0
        stack=[]
        for i in s:
            if i==')':
                if numOpen>0:
                    stack.append(i)
                    numOpen-=1
            elif i=='(':
                stack.append(i)
                numOpen+=1
            else:
                stack.append(i)
        numClose=0
        result=[]
        for i in stack[::-1]:
            if i==')':
                result.append(i)
                numClose+=1
            elif i=='(':
                if numClose>0:
                    result.append(i)
                    numClose-=1
            else:
                result.append(i)
        return "".join(result[::-1])
