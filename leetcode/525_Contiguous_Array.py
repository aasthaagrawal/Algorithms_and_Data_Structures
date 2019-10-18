#https://leetcode.com/problems/contiguous-array/
#Complexity: O(n)

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        d={}
        d[0]=-1
        maxLen=0
        sum=0
        for i in range(len(nums)):
            if nums[i]==0:
                sum-=1
            else:
                sum+=1
            if sum not in d:
                d[sum]=i
            else:
                maxLen=max(maxLen,i-d[sum])
        return maxLen
