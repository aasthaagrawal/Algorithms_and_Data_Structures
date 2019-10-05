#https://leetcode.com/problems/distance-between-bus-stops/
#Complexity: O(n)

class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        n=len(distance)
        total=sum(distance)
        oneRoute=0
        if start==destination:
            return 0
        elif start<destination:
            oneRoute=sum(distance[start:destination])
        else:
            oneRoute=sum(distance[destination:start])
        return min(oneRoute,total-oneRoute)
