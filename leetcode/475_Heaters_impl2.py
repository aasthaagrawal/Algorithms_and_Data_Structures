#https://leetcode.com/problems/heaters/
#Complexity: O(n+m)

class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()
        houses.sort()
        heaters=[float('-inf')]+heaters+[float('inf')]
        j=1
        n=len(heaters)
        maxdist=0
        for i in houses:
            while heaters[j]<i:
                j+=1
            r=min(i-heaters[j-1],heaters[j]-i)
            maxdist=max(maxdist,r)
        return maxdist
