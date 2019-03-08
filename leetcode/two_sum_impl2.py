#https://leetcode.com/problems/two-sum/
#Complexity O(n)

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic={}        
        length=len(nums)
            
        for i in range(length):
            if target-nums[i] in dic:
                return i, dic[target-nums[i]]
            dic[nums[i]]=i
