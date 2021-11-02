#https://leetcode.com/problems/cheapest-flights-within-k-stops/
#Time Complexity: O(EK)
#Space Complexity: O(V)

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        dist = [[float("inf")]*n for i in range(2)]
        dist[0][src] = dist[1][src] = 0
        for iteration in range(k+1):
            for s,d,w in flights:
                d_s = dist[1-(iteration&1)][s]
                d_d = dist[iteration&1][d]
                if d_s + w < d_d:
                    dist[iteration&1][d] = d_s + w
        return -1 if dist[k&1][dst]==float("inf") else dist[k&1][dst]
