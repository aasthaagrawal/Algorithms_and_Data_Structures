#https://leetcode.com/problems/permutations/
#Complexity: O(n!*n)

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result=[]
        def permuteUtil(l,r):
            if l==r:
                result.append(nums[:])
                return
            for i in range(l,r+1):
                nums[l],nums[i]=nums[i],nums[l]
                permuteUtil(l+1,r)
                nums[l],nums[i]=nums[i],nums[l]
        permuteUtil(0,len(nums)-1)
        return result
