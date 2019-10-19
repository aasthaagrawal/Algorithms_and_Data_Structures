#https://leetcode.com/problems/split-a-string-in-balanced-strings/
#Complexity: O(n)

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        result=0
        sum=0
        for i in s:
            if i=='R':
                sum+=1
            else:
                sum-=1
            if sum==0:
                result+=1
        return result
    
