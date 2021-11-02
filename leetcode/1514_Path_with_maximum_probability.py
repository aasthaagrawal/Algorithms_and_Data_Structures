#https://leetcode.com/problems/path-with-maximum-probability/
#Time complexity: O(ElogV)

class Solution:
    import heapq
    from collections import defaultdict

    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:

        self.graph = defaultdict(list)
        for i,edge in enumerate(edges):
            self.graph[edge[0]].append((edge[1], succProb[i]))
            self.graph[edge[1]].append((edge[0], succProb[i]))

        visited = [False]*n
        prob = [0 for i in range(n)]
        prob[start] = 1
        pq = [(-1,start)]
        heapq.heapify(pq)
        while pq:
            node_p,node = heapq.heappop(pq)
            if node == end:
                break
            if visited[node]:
                continue
            node_p *= -1
            visited[node] = True
            for i,p in self.graph[node]:
                if visited[i]:
                    continue
                new_prob = p*node_p
                if prob[i] == 0 or new_prob > prob[i]:
                    prob[i] = new_prob
                    heapq.heappush(pq, (-1*prob[i],i))
        return prob[end]
