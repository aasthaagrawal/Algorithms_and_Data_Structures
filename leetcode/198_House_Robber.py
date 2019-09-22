#https://leetcode.com/problems/house-robber/
#Compexity: O(n)

class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        if n==0:
            return 0
        elif n<3:
            return max(nums)
        dpAux=[0]*n
        dpAux[0]=nums[0]
        dpAux[1]=max(nums[0],nums[1])
        for i in range(2,n):
            dpAux[i]=max(dpAux[i-1],dpAux[i-2]+nums[i])
        return dpAux[-1]
