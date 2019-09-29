#https://leetcode.com/problems/heaters/
#Complexity: O(nlogm)

class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()
        n=len(heaters)
        maxdist=0
        for i in houses:
            maxdist=max(maxdist,self.heaterSearch(heaters,0,int((n-1)/2),n-1,i))   
        return maxdist
            
    def heaterSearch(self,heaters,l,m,h,i):
        if heaters[m]==i:
            return 0
        if heaters[m]<i:
            if m==h:
                return i-heaters[m]
            elif heaters[m+1]<i:
                return self.heaterSearch(heaters,m+1,int(m+1+(h-m-1)/2),h,i)
            else:
                return min(heaters[m+1]-i,i-heaters[m])
        if heaters[m]>i:
            if m==l:
                return heaters[m]-i
            elif heaters[m-1]>i:
                return self.heaterSearch(heaters,l,int(l+(m-1-l)/2),m-1,i)
            else:
                return min(heaters[m]-i,i-heaters[m-1])
