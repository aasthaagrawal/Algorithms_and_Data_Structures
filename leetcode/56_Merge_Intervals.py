#https://leetcode.com/problems/merge-intervals/
#Complexity: O(nlogn)

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n=len(intervals)
        if n<2:
            return intervals
        intervals.sort(key=lambda x:x[0])
        result=[]
        result.append(intervals[0])
        index=0
        for i in range(1,n):
            if intervals[i][0]<=result[index][1]:
                result[index][1]=max(intervals[i][1],result[index][1])
            else:
                result.append(intervals[i])
                index+=1
        return result
