#https://leetcode.com/problems/longest-turbulent-subarray/
#Complexity: O(n)

class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        if len(arr)<=1:
            return len(arr)
        lastSign = -1
        currLen = 1
        maxTurbSubarray = 1
        for i in range(1,len(arr)):
            sign = 1 if (arr[i-1]>arr[i]) else 0
            if (arr[i-1] == arr[i]):
                sign = -1
            if sign == -1:
                currLen = 1
                lastSign = -1
            else:
                if sign != lastSign:
                    currLen += 1
                    maxTurbSubarray = max(maxTurbSubarray, currLen)
                    lastSign = sign
                else:
                    currLen = 2
        return maxTurbSubarray
