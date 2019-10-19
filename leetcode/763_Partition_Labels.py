#https://leetcode.com/problems/partition-labels/
#Complexity: O(n)

class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        d={}
        n=len(S)
        for i in range(n):
            if S[i] in d:
                d[S[i]][-1]=i
            else:
                d[S[i]]=[i,i]
        start=0
        result=[]
        while start<n:
            end=d[S[start]][1]
            result.append(start)
            start+=1
            while start<=end:
                if d[S[start]][1]>end:
                    end=d[S[start]][1]
                start+=1
            result[-1]=end-result[-1]+1
        return result
