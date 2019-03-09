#https://leetcode.com/problems/3sum/
#Complexity O(n^2)

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        length=len(nums)
        solutionSet=set()
        dictionary={}
        for i in range(length):
            dictionary[nums[i]]=i
        
        for i in range(length-1):
            val1=nums[i]
            for j in range(i+1,length):
                val2=nums[j]
                reqVal=0-val1-val2
                if reqVal in dictionary and i!=dictionary[reqVal] and j!=dictionary[reqVal]:
                    solutionSet.add(tuple(sorted([val1,val2,reqVal])))
        
        return list(solutionSet)
