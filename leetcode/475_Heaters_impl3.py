#https://leetcode.com/problems/heaters/
#Complexity: O(nlog m)

class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()
        heaters=[float('-inf')]+heaters+[float('inf')]
        n=len(heaters)
        maxdist=0
        for i in houses:
            r=self.binSearch(heaters, 0,int((n-1)/2),n-1,i)
            maxdist=max(r,maxdist)
        return maxdist
    
    def binSearch(self,heaters,l,m,h,i):
        if heaters[m]==i:
            return 0
        if heaters[m]<i and heaters[m+1]>i:
            return min(i-heaters[m],heaters[m+1]-i)
        elif heaters[m]<i:
            return self.binSearch(heaters,m+1,int(m+1+(h-m-1)/2),h,i)
        elif heaters[m]>i and heaters[m-1]<i:
            return min(i-heaters[m-1],heaters[m]-i)
        else:
            return self.binSearch(heaters,l,int(l+(m-1-l)/2),m-1,i)
