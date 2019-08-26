#https://leetcode.com/problems/climbing-stairs/
#Complexity: O(n)

class Solution:
    def climbStairs(self, n: int) -> int:
        if n<3:
            return n
        a=[None]*2
        a[0]=1
        a[1]=2
        sum=0
        for i in range(2,n):
            sum=a[0]+a[1]
            a[0]=a[1]
            a[1]=sum
        return a[1]
