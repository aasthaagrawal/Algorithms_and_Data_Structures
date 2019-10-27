#https://leetcode.com/problems/subsets/
#Complexity: O(2^n)

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result=[]
        n=len(nums)
        if n==0:
            return [[]]
        def util(i,subset):
            print(subset)
            result.append(subset[:])
            for k in range(i,n):
                subset.append(nums[k])
                util(k+1,subset)
                subset.pop(-1)
            
            
        util(0,[])
        return result
