#https://leetcode.com/problems/combination-sum/
#Complexity: O(2^n)

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        n=len(candidates)
        if n==0:
            return []
        
        result=set()
        
        def util(subset,total,index):
            if total>target:
                return
            if total==target:
                result.add(tuple(subset[:]))
                return
            for i in range(index,n):
                subset.append(candidates[i])
                total+=candidates[i]
                util(subset,total,i)
                subset.pop(-1)
                total-=candidates[i]
        
        util([],0,0)
        return list(result)
