#https://leetcode.com/problems/top-k-frequent-elements/

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        sorted_d=sorted(d.items(),key= lambda x:x[1],reverse=True)[:k]
        result=[]
        for ele in sorted_d:
            result.append(ele[0])
        return result
