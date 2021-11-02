#https://leetcode.com/problems/cheapest-flights-within-k-stops/

class Solution:

    from collections import defaultdict
    import heapq

    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for flight in flights:
            graph[flight[0]].append((flight[1],flight[2]))

        k += 1
        numstops = [0]*n
        cost_arr = [float("inf")]*n
        cost_arr[src] = 0
        pq = [(0,src,0)] #cost,node,stops
        heapq.heapify(pq)
        while pq:
            cost,city,stops = heapq.heappop(pq)
            if city ==dst:
                return cost_arr[city]
            for i,c in graph[city]:
                new_cost = cost + c
                new_stop_count = stops + 1
                if new_stop_count <= k and new_cost < cost_arr[i]:
                    cost_arr[i] = new_cost
                    numstops[i] = new_stop_count
                    heapq.heappush(pq,(new_cost,i,new_stop_count))
                elif new_stop_count <= numstops[i]:
                    heapq.heappush(pq,(new_cost,i,new_stop_count))
        return -1
