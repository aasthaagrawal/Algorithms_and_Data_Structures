#https://leetcode.com/problems/remove-outermost-parentheses/
#Time complexity: O(n)
#Space complexity: O(n)

class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        result = ""
        st = []
        start = 0
        for i,ele in enumerate(s):
            if ele=='(':
                st.append(ele)
            else:
                st.pop(-1)
                if len(st)==0:
                    result = result + s[start+1:i]
                    start = i+1
        return result
