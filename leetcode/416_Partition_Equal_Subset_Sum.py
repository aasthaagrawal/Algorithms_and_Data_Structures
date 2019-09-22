#https://leetcode.com/problems/partition-equal-subset-sum/
#Complexity: O(lenNums*target)

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sumNums=sum(nums)
        lenNums=len(nums)
        if sumNums%2==1:
            return False
        target=sumNums//2
        if target<max(nums):
            return False
        dpAux=[False]*(target+1)
        dpAux[0]=True
        for i in nums:
            for j in range(target,0,-1):
                if j-i>=0:
                    dpAux[j]=dpAux[j] or dpAux[j-i]
        return dpAux[target]
