#https://leetcode.com/problems/3sum/
#Complexity O(n^3)

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        SolutionList=[]
        length=len(nums)
        nums.sort()
        for i in range(length-2):
            if i==0 or nums[i]!=nums[i-1]:
                for j in range(i+1,length-1):
                    if j==i+1 or nums[j]!=nums[j-1]:
                        for k in range(j+1,length):
                            if k==j+1 or nums[k]!=nums[k-1]:
                                if nums[i]+nums[j]+nums[k]==0:
                                    temp=[nums[i],nums[j],nums[k]]
                                    temp.sort()
                                    SolutionList.append(temp)
        return SolutionList
