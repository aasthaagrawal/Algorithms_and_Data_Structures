#https://leetcode.com/problems/generate-parentheses/
#Complexity: O((4^n)/(nsqrtn))
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result=[]
        if n==0:
            return result
        
        def util(numOpen,numClose,sol):
            if numOpen==0 and numClose==0:
                result.append(''.join(sol[:]))
                return
            if numOpen>0:
                sol.append("(")
                util(numOpen-1,numClose+1,sol)
                sol.pop(-1)
            if numClose>0:
                sol.append(")")
                util(numOpen,numClose-1,sol)
                sol.pop(-1)

        util(n,0,[])
        return result
