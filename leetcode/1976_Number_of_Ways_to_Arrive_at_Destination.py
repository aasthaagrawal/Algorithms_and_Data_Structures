#https://leetcode.com/problems/number-of-ways-to-arrive-at-destination/
#Time complexity: O((E+V) log V)
class Solution:
    import heapq
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        #construct graph
        graph = {i:[] for i in range(n)}
        for u,v,w in roads:
            graph[u].append((v,w))
            graph[v].append((u,w))

        visited = [False]*n
        dp = [[float("inf"), 0] for i in range(n)] #minDist, numWays
        dp[0] = [0,1]
        shortestPath = [(0,0)] #minDist, nodeNum
        heapq.heapify(shortestPath)
        node = heapq.heappop(shortestPath)
        while node[1] != n-1:
            minDist, nodeNum, numWays = node[0], node[1], dp[node[1]][1]
            if not visited[nodeNum]:
                visited[nodeNum] = True
                for v,w in graph[nodeNum]:
                    if not visited[v]:
                        new_dist = w+minDist
                        if new_dist == dp[v][0]:
                            dp[v][1] += numWays
                        elif new_dist < dp[v][0]:
                            dp[v][0] = new_dist
                            dp[v][1] = numWays
                            heapq.heappush(shortestPath, (new_dist, v))
            node = heapq.heappop(shortestPath)

        return dp[-1][1]%(pow(10,9)+7)
