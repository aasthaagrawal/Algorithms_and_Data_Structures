#https://leetcode.com/problems/missing-number/
#Complexity: O(n)

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        lenArr=len(nums)
        sumres=int(((lenArr+1)*lenArr)/2)
        for i in range(lenArr):
            sumres-=nums[i]
        return sumres
