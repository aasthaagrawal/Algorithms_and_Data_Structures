#https://leetcode.com/problems/maximum-sum-circular-subarray/

class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        
        total = 0
        minSum = float("inf")
        maxSum = -float("inf")
        currMaxSum = 0
        currMinSum = 0
        for i in A:
            total += i
            currMaxSum = i + max(0,currMaxSum)
            maxSum = max(maxSum,currMaxSum)
            currMinSum = i + min(0,currMinSum)
            minSum = min(minSum, currMinSum)
        
        #Handling case when all elements are negative
        #In this case we need to return the maxElement
        if total == minSum:
            return maxSum
        return max(maxSum, total - minSum)
