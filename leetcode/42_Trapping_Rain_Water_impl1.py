#https://leetcode.com/problems/trapping-rain-water/
#Complexity:O(n)

class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        left=[0]*n
        if n<=0:
            return 0
        left[0]=height[0]
        minArr=[0]*n
        right_max=0
        result=0
        for i in range(1,n):
            left[i]=max(left[i-1],height[i])
        for i in range(n-1,-1,-1):
            right_max=max(right_max,height[i])
            minArr[i]=min(right_max,left[i])
            if minArr[i]>height[i]:
                result+=(minArr[i]-height[i])
        return result
