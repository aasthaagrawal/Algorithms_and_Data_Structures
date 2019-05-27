#https://leetcode.com/problems/valid-parentheses/
#Complexity: O(n)

class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        mapping={")":"(", "]":"[","}":"{"}
        for ch in s:
            if ch in mapping:
                if stack:
                    top=stack.pop()
                    if not top==mapping[ch]:
                        return False
                else:
                    return False
            else:
                stack.append(ch)
        if len(stack)==0:
            return True
        return False
